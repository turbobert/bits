# German Cherry Keyboard on a MacBook Pro 2019

I trashed my apple keyboard with coffee. Tried a *German* layout'ed

    Cherry KC 6000 SLIM for MAC

which I actually like quite well. But

    <
    ^

are mixed up. On the external. The internal is fine. Also fn sucks.

So to fix the external (which breaks the internal while active) I switched 0x64 with 0x35 and all fine.

    hidutil property --set '{"UserKeyMapping": [{"HIDKeyboardModifierMappingSrc": 0x700000064, "HIDKeyboardModifierMappingDst": 0x700000035},{"HIDKeyboardModifierMappingSrc": 0x700000035, "HIDKeyboardModifierMappingDst": 0x700000064}]}'

To go back to your internal layout just run
    
    hidutil property --set '{"UserKeyMapping": []}'

again.

Note: to play around, I used 0x39 a lot as source (caps lock) to *not* lock me out.

See https://gist.github.com/MightyPork/6da26e382a7ad91b5496ee55fdc73db2
