# Emoji
To display properly (full color) on a system like Windows, emoji UTF-8 codes
must include the `b"\xef\xb8\x8f"` suffix. Not certain why.
- The built-in emoji selector in Windows does not always include this suffix.
- The "convert_to_emoji.py" script generates takes a partially generated emoji,
  and appends this suffix if it is missing. The result displays correctly in
  most Windows text editors.


