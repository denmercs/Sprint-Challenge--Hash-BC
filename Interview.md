================================================== ANSWER ==================================================

- Explain in detail the workings of a dynamic array:

Dynamic array has a larger capacity or space that it basically needs. while also storing its size on the array.
Once the array is full it will create another similar size/capacity of the array.

The advantage for this is to be able to add and remove data from the array quickly but adds up memory.

================================================== ANSWER ==================================================

- What is the runtime complexity to access an array, add or remove from the front, and add or remove from the back?

ANSWER:

add/remove (front) --> O(n) --> need to shift the indexes to the right
add/remove (back) --> O(1) --> just add the respective indexes of the array

================================================== ANSWER ==================================================

- What is the worse case scenario if you try to extend the storage size of a dynamic array?

ANSWER:

But if the dynamic array doesn't have any room for the new item, it'll need to expand, which takes O(n) time.

Copying each item over costs O(n) time! So whenever appending an item to our dynamic array forces us to make a new double-size underlying array, that append takes O(n)O(n) time.

That's the worst case. But in the best case (and the average case), appends are just O(1)O(1) time.

================================================== ANSWER ==================================================
Explain how a blockchain is structured. What are the blocks, what is the chain? How is the data organized?

- It has a block, chain, hash from itself and a previous hash

[data / block] <-- hashes prev--> [data / block] <-- hashes prev>

- changing something to the block the hash will change
- hash of the previous block
- first block is special which is (genesis block)

---

================================================== ANSWER ==================================================
Explain how proof of work functions. How does it operate. How does this protect the chain from attack. What kind of attack is possible?

- it's not enough to prevent tampering which you can just recalculate the hashes and just duplicate the inserted block
- Proof of work (Slow and steady) solution will be proof of work, it slows down the creation of creating a new block in case of bitcoin it has 10 min.

* distributed (peer to peer network). The node will verify everyone to every network and everything checks out, each nodes add block to the block chain.
