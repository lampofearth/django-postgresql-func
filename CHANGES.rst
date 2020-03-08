=========
Changelog
=========

Release 0.0.1
==============
*Released 1900-01-01*

First release

**New features:**

Implemented String Functions:

- ``BitLen`` as sql BIT_LENGTH(string)
- ``CharLen`` as CHAR_LENGTH(string)
- ``OctetLen`` as OCTET_LENGTH(string)
- ``Overlay`` as OVERLAY(string PLACING string FROM int [FOR int])
- ``Position`` as POSITION(substring in string)
- ``Btrim`` as BTRIM(string text [, characters text])
- ``InitCap`` as INITCAP(string)
- ``QuoteIdent`` as QUOTE_IDENT(string text)
- ``QuoteLiteral`` as QUOTE_LITERAL(string text)
- ``QuoteNullable`` as QUOTE_NULLABLE(string text)
- ``SplitPart`` as SPLIT_PART(string text, delimiter text, field int)
- ``StrPos`` as STRPOS(string, substring)
- ``ToHex`` as TO_HEX(number)
- ``Translate`` as TRANSLATE(string text, from text, to text)

Implemented Math Functions:

- ``Cbrt`` as sql CBRT(value)
- ``Div`` as sql DIV(y, x)
- ``Trunc`` as sql TRUNC(value, plc=0)