import functools
list_Atr = ["STR","DEX","CON","INT","WIZ","CHA"]
class Tag:
    """
    A dynamic and fluent tag generator. It automatically creates and caches
    tagger objects for different UI panels, enforcing a strict and consistent
    naming convention everywhere.
    """
    def __init__(self):
        self._cache = {}

    @staticmethod
    def _format_part(part: str) -> str:
        part_str = str(part)
        if part_str in list_Atr:
            return part_str
        return part_str.replace('_', ' ').title().replace(' ', '_')

    def __getattr__(self, panel_name: str) -> 'Tagger':
        formatted_panel = self._format_part(panel_name)
        if formatted_panel not in self._cache:
            self._cache[formatted_panel] = self.Tagger(formatted_panel, self._format_part)
        return self._cache[formatted_panel]

    class Tagger:
        def __init__(self, prefix: str, formatter: callable):
            self._prefix = prefix
            self._format = formatter

        def __getattr__(self, suffix: str) -> callable:
            formatted_suffix = self._format(suffix)
            @functools.wraps(self._build_tag)
            def tag_builder(*identifiers):
                return self._build_tag(formatted_suffix, *identifiers)
            return tag_builder

        def _build_tag(self, suffix: str, *identifiers) -> str:
            parts = [self._prefix]
            if identifiers:
                parts.extend(self._format(i) for i in identifiers)
            parts.append(suffix)
            return "_".join(parts)
