**Draft: this repo is in quiet mode, thanks**

LiuCipher (LC) is a security protocol.

This software is implemented in Python. It allows two nodes to establish a shared private key over an open network -- try it out!

LC aims to be the new standard for encryption. **_Assuming it cannot be cracked_**, it is better than other protocols in the following ways:

* It uses randomly generated keys, meaning **no amount of computational power can decipher intercepted messages.**
* It is symmetric (single key used to encrypt and decrypt), but unlike other symmetric ciphers; LC allows Alice and Bob to generate a key over an **insecure channel** like the web.

**Your task**, should you choose to accept it, is to crack LC. In this implementation, LC uses a psuedo-random number generator - the Mersenne Twister. Exploiting the RNG is not a true crack. A valid crack entails exploiting weakness(es) - if any - in the protocol itself.  However, any crack is interesting and worth attempting. A passive attack by signal analysis is one potential path.

To make the game **clear**, assume Alice and Bob can only communicate via Eve. Before commencing key negotiation, Alice and Bob are reasonably confident the other is whom they claim to be -- the two also share an info-theoretic-secure authenticated public channel to facilitate key reconciliation [though such channel is not in this implementation]. 

Also, Eve's computer answers NP-hard questions in P. She has full read/write capability over any transmission, and is blind to Alice / Bob's internal state.

Documentation can be found in **/doc/index.rst**

Optimal parameter settings are: -n 1250 -tr 20

ッ

----------------------------------------------

_Copyright 1992-2015 The FreeBSD Project. All rights reserved._

_Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:_

    Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
    Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

_**THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS ``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.**_

