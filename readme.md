«Memorize Morse in one sentence.»

### my love life has a vibe, the same as edgy pop star DJ «Dr BBQ» adds — glad she won't cut away all good gold lyre!

Code
====
There are 26 words in that sentence, like 26 letters.

```
my love life has a vibe, the same as edgy pop star DJ «Dr BBQ» adds
A   B    C    D  E  F     G   H   I   J    K   L   M   N   O    P  

 — glad she won't cut away all good gold lyre!
    Q    R   S  T  U   V    W   X    Y    Z
```

In each word, "tall" letters (letters with an ascender or descender: bdfghjklpqty) represent dashes,
while "short" letters (letters the same height as "x": aceimnorsuvwxz) represent dots:

```
my  love  life  has  a  vibe,  the  same  as  edgy  pop  star  DJ  «Dr  BBQ»  adds
.|  |...  |.|.  |..  .  ..|.   ||.  ....  ..  .|||  |.|  .|..  ||   |.  |||   .||.
.-  -...  -.-.  -..  .  ..-.   --.  ....  ..  .---  -.-  .-..  --   -.  ---   .--.
A    B     C     D   E   F      G    H    I    J     K    L    M    N    O     P


  —  glad  she  won't  cut  away  all  good  gold  lyre!
     ||.|  .|.  ...  |  ..|  ...|  .||  |..|  |.||  ||..
     --.-  .-.  ...  -  ..-  ...-  .--  -..-  -.--  --..
      Q     R    S   T   U    V     W    X     Y     Z
```

Repeat the sentence a few times. (Now.)<br>
You've just "memorized" the Morse code.

Goal
====
Let's state the goal so you know whether this is of interest to you:
The goal is to be able to reconstitute Morse code in a few minutes, by heart, in several years, without practising much in between.
Pretend you might be some day in an extreme case like Jeremiah Denton.
Or in the movie «Executive Decision» (spoiler: https://www.youtube.com/watch?v=cNl8HigtLzE).
You need to send a Morse message once, you've got some time to encode it,
you don't have access to any material: you must work from what you already know.

The goal is not to be able to send/receive messages in Morse after just learning this mnemonic.
For that, one should practice a lot and get an instant association between the sound and the letter.
The goal is only to have memorized enough information so that one is able, with some more work, to slowly encode/decode Morse.

Morse mnemonics
===============

I've seen various mnemonic to learn the Morse code.
For instance, a drawing for each letter to bring to life the dots and dashes, or dots and dashes drawn inside each letter.
I wasn't satisfied because they treat each letter independently, so it's easy to forget the code of one letter.
They are intended to be a help during learning. I have a different goal.

One of those mnemonics got me interested: the idea of William Harder to represent each morse codepoint by a word;
the letters of the word being each a dot or a dash.
Namely bdfghjklpqty encode dashes, while aceimnorsuvwxz encode dots:
the first group are "tall" letters (letters with an ascender or a descender) while the second group are letters with the same height as "x".
For instance, "foxy" is read as |..|, or -..-, which is morse code for "X".
Douglas Wilhelm Harder then chose 26 words to memorize each morse codepoint.

I wanted to take this idea one step further: what is a sequence of words? A sentence!
Plus, a sentence should be easier to memorize than a list of unrelated words,
its meaning and its flow helping to memorize it.

So I set out to find a sentence of 26 words with this constraint: the nth word must represent the morse code of the nth letter of the alphabet (easy).
The sentence should somewhat make sense (hard).

For instance, the tenth word must represent J, or `.---`, ie one of [aceimnorsuvwxz] followed by three letters among [bdfghjklpqty].
There aren't so many words, the most common ones are "ably ally eddy edgy idly idyl iffy myth ugly".
(Some other letters have more possible words).


Programming
===========
I first tried a greedy algorithm: pick words one by one and grow the sentence until the 26th word.
I used the large language model GPT2 and its encapsulation in the python package lm_scorer.
That allows to programmaticaly get an approximate "readability" score of the sentence.
The algorithm is thus:

```
for i from 1 to 26:
  go through all possible words for the ith letter
    for each word, tentatively add it to the sentence, score the result
  pick one of those words at random, with a probability proprotionnal to the readability score

repeat many times and surface the most readable sentences
```

Also, try each word with and without a comma.
It got some nice findings, but nothing good enough.

I then tried a genetic algorithm, the vanilla way.
(Mutate by replacing one word at random, cross two sentences by inserting the middle of one into the other one.)
It was slower and got no better results.
I finally refined the best results by hand, taking heavy inspiration and trying many excerpts from the sentences the algorithms found.
Sometimes I went manually trough all possible words at a given position.
I rejected sentences because of grammar, of gibberish meaning, of sad or slang words, of hard pronunciation, of obscure rare words, etc.
I had to compromise and accepted the need for some punctuation.
Here is the result:

### my love life has a vibe, the same as edgy pop star DJ «Dr BBQ» adds — glad she won't cut away all good gold lyre!

I'm happy to read about improvements if you want to try (beware it's difficult)!

Wait, new idea!
===============
Instead of "tall" / "short" letters, the alphabet partition could be into
"letters whith a hole" (abdegopq) / remaining letters (cfhijklmnrstuvwxyz)
The advantage is that vowels are more evenly distributed among both groups, so there should be fewer problematic codepoints.
Well, scratch that, it seems harder to mentally convert a word into a code. The alphabet partition is less visual.

## Hope you liked it!

This work is licensed under a <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0 license</a>.