"""
Banjo-Kazooie Archipelago World Debug Module

This module provides comprehensive debugging for tracking:
1. Item/location count mismatches
2. Generation failures
3. Unreachable locations
4. Logic rule issues
5. Item placement problems

Usage:
    Add these imports to __init__.py:
        from .bk_debug import BKDebugger
    
    Then instantiate and use in your World class:
        self.debugger = BKDebugger(self)
        self.debugger.log_generation_start()
        # ... after create_items ...
        self.debugger.log_items_created()
        # ... after create_regions ...
        self.debugger.log_regions_created()
        # ... after set_rules ...
        self.debugger.log_rules_set()
        # At end of generation
        self.debugger.log_generation_complete()
        self.debugger.write_debug_report()
"""

import logging
from typing import TYPE_CHECKING, Dict, List, Set, Optional, Any
from collections import defaultdict

if TYPE_CHECKING:
    from . import BKWorld

# Set up a dedicated logger for BK debugging
logger = logging.getLogger("BK_Debug")


class BKDebugger:
    """Debug helper for Banjo-Kazooie Archipelago World generation."""
    
    def __init__(self, world: "BKWorld", verbose: bool = True):
        self.world = world
        self.player = world.player
        self.mw = world.multiworld
        self.options = world.options
        self.verbose = verbose
        
        # Track statistics
        self.stats: Dict[str, Any] = {
            "items_created": {},
            "locations_created": {},
            "locked_locations": {},
            "regions_created": [],
            "exits_created": {},
            "rules_applied": {"regions": 0, "locations": 0},
            "errors": [],
            "warnings": [],
        }
        
        self._setup_logging()
    
    def _setup_logging(self):
        """Configure logging for debug output."""
        if not logger.handlers:
            handler = logging.StreamHandler()
            handler.setLevel(logging.DEBUG)
            formatter = logging.Formatter(
                '[BK P%(player)s] %(levelname)s: %(message)s'
            )
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        logger.setLevel(logging.DEBUG if self.verbose else logging.INFO)
    
    def _log(self, level: str, msg: str):
        """Log a message with player context."""
        extra = {"player": self.player}
        getattr(logger, level)(msg, extra=extra)
    
    def debug(self, msg: str):
        self._log("debug", msg)
    
    def info(self, msg: str):
        self._log("info", msg)
    
    def warning(self, msg: str):
        self.stats["warnings"].append(msg)
        self._log("warning", msg)
    
    def error(self, msg: str):
        self.stats["errors"].append(msg)
        self._log("error", msg)

    # =========================================================================
    # Generation Phase Logging
    # =========================================================================
    
    def log_generation_start(self):
        """Call at the beginning of world generation."""
        self.info("=" * 60)
        self.info("Starting Banjo-Kazooie World Generation")
        self.info("=" * 60)
        self._log_options()
    
    def _log_options(self):
        """Log current options."""
        self.info("Options:")
        self.debug(f"  logic_difficulty: {self.options.logic_difficulty.value}")
        self.debug(f"  notesanity: {self.options.notesanity.value}")
        self.debug(f"  talon_lobby: {self.options.talon_lobby.value}")
        self.debug(f"  extra_locations: {self.options.extra_locations.value}")
    
    def log_items_created(self):
        """Call after create_items() to analyze item pool."""
        from .Items import item_data_table
        
        self.info("-" * 40)
        self.info("Analyzing Item Pool")
        self.info("-" * 40)
        
        # Count items in pool for this player
        player_items: Dict[str, int] = defaultdict(int)
        for item in self.mw.itempool:
            if item.player == self.player:
                player_items[item.name] += 1
        
        self.stats["items_created"] = dict(player_items)
        
        # Check expected vs actual
        expected_items: Dict[str, int] = {}
        for name, item_data in item_data_table.items():
            if item_data.code and item_data.can_create(self.options):
                expected_items[name] = item_data.num_exist
        
        total_expected = sum(expected_items.values())
        total_actual = sum(player_items.values())
        
        self.info(f"Total items expected: {total_expected}")
        self.info(f"Total items created: {total_actual}")
        
        if total_expected != total_actual:
            self.warning(f"MISMATCH: Expected {total_expected}, got {total_actual}")
        
        # Check for missing items
        for name, expected_count in expected_items.items():
            actual_count = player_items.get(name, 0)
            if actual_count != expected_count:
                self.warning(f"  Item '{name}': expected {expected_count}, got {actual_count}")
        
        # Log progression items specifically
        self.debug("Progression items in pool:")
        from BaseClasses import ItemClassification
        for name, count in sorted(player_items.items()):
            item_data = item_data_table.get(name)
            if item_data and item_data.type == ItemClassification.progression:
                self.debug(f"  {name}: {count}")
    
    def log_regions_created(self):
        """Call after create_regions() to analyze region/location setup."""
        from .Locations import location_data_table, locked_locations
        from .Regions import region_data_table
        
        self.info("-" * 40)
        self.info("Analyzing Regions and Locations")
        self.info("-" * 40)
        
        # Count regions
        player_regions = [r for r in self.mw.regions if r.player == self.player]
        self.stats["regions_created"] = [r.name for r in player_regions]
        self.info(f"Regions created: {len(player_regions)}")
        
        # Expected regions
        expected_regions = len(region_data_table)
        if len(player_regions) != expected_regions:
            self.warning(f"Region count mismatch: expected {expected_regions}, got {len(player_regions)}")
        
        # Analyze locations per region
        total_locations = 0
        locations_by_region: Dict[str, List[str]] = defaultdict(list)
        
        for region in player_regions:
            for loc in region.locations:
                locations_by_region[region.name].append(loc.name)
                total_locations += 1
        
        self.stats["locations_created"] = dict(locations_by_region)
        
        # Count expected locations
        expected_locations = 0
        expected_by_region: Dict[str, int] = defaultdict(int)
        for loc_name, loc_data in location_data_table.items():
            if loc_data.can_create(self.options):
                expected_locations += 1
                expected_by_region[loc_data.region] += 1
        
        self.info(f"Total locations expected: {expected_locations}")
        self.info(f"Total locations created: {total_locations}")
        
        if total_locations != expected_locations:
            self.warning(f"Location count mismatch: expected {expected_locations}, got {total_locations}")
            
            # Show per-region breakdown
            for region_name in sorted(set(list(expected_by_region.keys()) + list(locations_by_region.keys()))):
                expected = expected_by_region.get(region_name, 0)
                actual = len(locations_by_region.get(region_name, []))
                if expected != actual:
                    self.warning(f"  Region '{region_name}': expected {expected}, got {actual}")
        
        # Analyze locked locations
        locked_count = 0
        for loc_name, loc_data in locked_locations.items():
            if loc_data.can_create(self.options):
                locked_count += 1
                loc = self.mw.get_location(loc_name, self.player)
                if loc.item:
                    self.stats["locked_locations"][loc_name] = loc.item.name
                    self.debug(f"  Locked: '{loc_name}' -> '{loc.item.name}'")
                else:
                    self.warning(f"  Locked location '{loc_name}' has no item!")
        
        self.info(f"Locked locations: {locked_count}")
        
        # Check notesanity placements
        if not self.options.notesanity.value:
            note_placements = 0
            for loc_name, loc_data in location_data_table.items():
                if loc_data.address is not None and (loc_data.address & 0xFF000000) == 0x01000000:
                    try:
                        loc = self.mw.get_location(loc_name, self.player)
                        if loc.item and loc.item.name == "Note":
                            note_placements += 1
                    except KeyError:
                        pass
            self.info(f"Note placements (notesanity off): {note_placements}")
        
        # Analyze exits
        for region in player_regions:
            exits = [e.name for e in region.exits]
            if exits:
                self.stats["exits_created"][region.name] = exits
                self.debug(f"Region '{region.name}' exits: {exits}")
    
    def log_rules_set(self):
        """Call after set_rules() to analyze access rules."""
        self.info("-" * 40)
        self.info("Analyzing Access Rules")
        self.info("-" * 40)
        
        # Count rules applied
        rules_on_entrances = 0
        rules_on_locations = 0
        
        player_regions = [r for r in self.mw.regions if r.player == self.player]
        
        for region in player_regions:
            for entrance in region.entrances:
                if entrance.access_rule is not None:
                    # Check if it's not the default "always true" rule
                    try:
                        # Default rule returns True for empty state
                        from BaseClasses import CollectionState
                        test_state = CollectionState(self.mw)
                        if not entrance.access_rule(test_state):
                            rules_on_entrances += 1
                    except:
                        rules_on_entrances += 1
            
            for location in region.locations:
                if location.access_rule is not None:
                    try:
                        from BaseClasses import CollectionState
                        test_state = CollectionState(self.mw)
                        if not location.access_rule(test_state):
                            rules_on_locations += 1
                    except:
                        rules_on_locations += 1
        
        self.stats["rules_applied"]["regions"] = rules_on_entrances
        self.stats["rules_applied"]["locations"] = rules_on_locations
        
        self.info(f"Entrance rules applied: {rules_on_entrances}")
        self.info(f"Location rules applied: {rules_on_locations}")
        
        if self.options.logic_difficulty.value == 4:
            self.info("Logic difficulty is 'no_logic' - minimal rules expected")
    
    def log_generation_complete(self):
        """Call at end of generation to provide summary."""
        self.info("=" * 60)
        self.info("Generation Complete - Final Analysis")
        self.info("=" * 60)
        
        # Check item/location balance
        total_items = sum(self.stats["items_created"].values())
        total_locations = sum(len(locs) for locs in self.stats["locations_created"].values())
        locked_count = len(self.stats["locked_locations"])
        
        # Available locations = total - locked
        available_locations = total_locations - locked_count
        
        self.info(f"Items in pool: {total_items}")
        self.info(f"Total locations: {total_locations}")
        self.info(f"Locked locations: {locked_count}")
        self.info(f"Available locations for pool: {available_locations}")
        
        if total_items > available_locations:
            self.error(f"MORE ITEMS THAN LOCATIONS: {total_items} items > {available_locations} available locations")
            self.error(f"  Excess: {total_items - available_locations} items cannot be placed!")
        elif total_items < available_locations:
            diff = available_locations - total_items
            self.warning(f"Fewer items than locations: {diff} locations will need filler")
        else:
            self.info("Item/location count is balanced")
        
        # Summary of issues
        if self.stats["errors"]:
            self.info("-" * 40)
            self.info(f"ERRORS ({len(self.stats['errors'])}):")
            for err in self.stats["errors"]:
                self.info(f"  - {err}")
        
        if self.stats["warnings"]:
            self.info("-" * 40)
            self.info(f"WARNINGS ({len(self.stats['warnings'])}):")
            for warn in self.stats["warnings"]:
                self.info(f"  - {warn}")

    # =========================================================================
    # Advanced Debugging Methods
    # =========================================================================
    
    def analyze_reachability(self, verbose: bool = False):
        """
        Analyze which locations are reachable with all items.
        Call this after fill_slot_data or at end of generation.
        """
        from BaseClasses import CollectionState
        
        self.info("-" * 40)
        self.info("Analyzing Location Reachability")
        self.info("-" * 40)
        
        # Create a state with all items
        state = CollectionState(self.mw)
        for item in self.mw.itempool:
            if item.player == self.player:
                state.collect(item)
        
        # Also add locked items
        player_regions = [r for r in self.mw.regions if r.player == self.player]
        for region in player_regions:
            for location in region.locations:
                if location.item and location.item.player == self.player:
                    state.collect(location.item, prevent_sweep=True)
        
        state.sweep_for_advancements(self.mw)
        
        reachable = []
        unreachable = []
        
        for region in player_regions:
            for location in region.locations:
                if location.can_reach(state):
                    reachable.append(location.name)
                else:
                    unreachable.append(location.name)
        
        self.info(f"Reachable locations (with all items): {len(reachable)}")
        self.info(f"Unreachable locations: {len(unreachable)}")
        
        if unreachable:
            self.warning("Unreachable locations detected!")
            for loc_name in sorted(unreachable)[:20]:  # Show first 20
                self.warning(f"  - {loc_name}")
            if len(unreachable) > 20:
                self.warning(f"  ... and {len(unreachable) - 20} more")
        
        return reachable, unreachable
    
    def check_progression_chain(self):
        """
        Check if all progression items can be obtained.
        This helps identify logic deadlocks.
        """
        from BaseClasses import CollectionState, ItemClassification
        
        self.info("-" * 40)
        self.info("Checking Progression Chain")
        self.info("-" * 40)
        
        state = CollectionState(self.mw)
        
        # Collect items in sphere order
        sphere = 0
        collected_this_sphere = True
        all_progression = set()
        collected_progression = set()
        
        # Identify all progression items
        for item in self.mw.itempool:
            if item.player == self.player and item.classification == ItemClassification.progression:
                all_progression.add(item.name)
        
        while collected_this_sphere:
            collected_this_sphere = False
            sphere += 1
            
            self.debug(f"Sphere {sphere}:")
            
            # Find reachable locations
            player_regions = [r for r in self.mw.regions if r.player == self.player]
            for region in player_regions:
                for location in region.locations:
                    if location.item and location.can_reach(state):
                        item = location.item
                        if item.player == self.player and item.name not in collected_progression:
                            if item.classification == ItemClassification.progression:
                                collected_progression.add(item.name)
                                self.debug(f"  Found: {item.name}")
                                collected_this_sphere = True
                                state.collect(item)
        
        missing = all_progression - collected_progression
        if missing:
            self.warning(f"Unable to collect {len(missing)} progression items:")
            for item_name in sorted(missing):
                self.warning(f"  - {item_name}")
        else:
            self.info("All progression items are reachable")
        
        return collected_progression, missing
    
    def dump_location_rules(self, region_filter: Optional[str] = None):
        """
        Dump all location access rules for debugging.
        Optionally filter by region name substring.
        """
        from .NormalRules import get_location_rules
        
        self.info("-" * 40)
        self.info(f"Location Rules Dump{f' (filter: {region_filter})' if region_filter else ''}")
        self.info("-" * 40)
        
        player_regions = [r for r in self.mw.regions if r.player == self.player]
        
        for region in player_regions:
            if region_filter and region_filter.lower() not in region.name.lower():
                continue
            
            self.debug(f"Region: {region.name}")
            for location in region.locations:
                rule_str = "None (always accessible)"
                if location.access_rule:
                    # Try to get some info about the rule
                    rule_str = str(location.access_rule)
                    if hasattr(location.access_rule, '__name__'):
                        rule_str = location.access_rule.__name__
                self.debug(f"  {location.name}: {rule_str[:80]}")
    
    def write_debug_report(self, filepath: str = "/tmp/bk_debug_report.txt"):
        """Write a comprehensive debug report to file."""
        import json
        
        with open(filepath, 'w') as f:
            f.write("=" * 60 + "\n")
            f.write("Banjo-Kazooie Archipelago Debug Report\n")
            f.write(f"Player: {self.player}\n")
            f.write("=" * 60 + "\n\n")
            
            f.write("OPTIONS:\n")
            f.write(f"  logic_difficulty: {self.options.logic_difficulty.value}\n")
            f.write(f"  notesanity: {self.options.notesanity.value}\n")
            f.write(f"  talon_lobby: {self.options.talon_lobby.value}\n")
            f.write(f"  extra_locations: {self.options.extra_locations.value}\n\n")
            
            f.write("STATISTICS:\n")
            f.write(f"  Items created: {sum(self.stats['items_created'].values())}\n")
            f.write(f"  Regions: {len(self.stats['regions_created'])}\n")
            total_locs = sum(len(v) for v in self.stats['locations_created'].values())
            f.write(f"  Locations: {total_locs}\n")
            f.write(f"  Locked locations: {len(self.stats['locked_locations'])}\n\n")
            
            if self.stats["errors"]:
                f.write("ERRORS:\n")
                for err in self.stats["errors"]:
                    f.write(f"  - {err}\n")
                f.write("\n")
            
            if self.stats["warnings"]:
                f.write("WARNINGS:\n")
                for warn in self.stats["warnings"]:
                    f.write(f"  - {warn}\n")
                f.write("\n")
            
            f.write("DETAILED ITEM COUNTS:\n")
            for name, count in sorted(self.stats["items_created"].items()):
                f.write(f"  {name}: {count}\n")
            f.write("\n")
            
            f.write("LOCATIONS BY REGION:\n")
            for region, locs in sorted(self.stats["locations_created"].items()):
                f.write(f"  {region}: {len(locs)} locations\n")
        
        self.info(f"Debug report written to: {filepath}")


def quick_debug_check(world: "BKWorld") -> Dict[str, Any]:
    """
    Quick one-liner debug check. Returns dict of potential issues.
    
    Usage in __init__.py:
        from .bk_debug import quick_debug_check
        # At end of set_rules:
        issues = quick_debug_check(self)
        if issues:
            print(f"BK Debug Issues: {issues}")
    """
    from .Items import item_data_table
    from .Locations import location_data_table, locked_locations
    
    issues = {}
    
    # Count items
    player_items = sum(1 for item in world.multiworld.itempool if item.player == world.player)
    
    # Count expected items
    expected_items = sum(
        item.num_exist for item in item_data_table.values()
        if item.code and item.can_create(world.options)
    )
    
    if player_items != expected_items:
        issues["item_count_mismatch"] = f"Expected {expected_items}, got {player_items}"
    
    # Count locations
    player_locations = sum(
        len(list(r.locations)) for r in world.multiworld.regions if r.player == world.player
    )
    
    expected_locations = sum(
        1 for loc in location_data_table.values()
        if loc.can_create(world.options)
    )
    
    if player_locations != expected_locations:
        issues["location_count_mismatch"] = f"Expected {expected_locations}, got {player_locations}"
    
    # Check balance
    locked_count = sum(
        1 for loc in locked_locations.values()
        if loc.can_create(world.options)
    )
    
    available = player_locations - locked_count
    if player_items > available:
        issues["more_items_than_locations"] = f"{player_items} items > {available} available locations"
    
    return issues
