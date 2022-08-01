<h1 align="center">103cipher</h1>

![image](https://user-images.githubusercontent.com/91891487/182234365-d122beba-57d4-4a02-a1c6-5aeb3e831409.png)

<h2> Description </h2>

<p>Cryptography is a very old science, whose goal is to secure communication, so that only its recipient could
read it.</p>
<p>There are a lot of methods to encrypt a message, from the simplest (such as the 2,000-year-old Caesar
cipher) to the most complex (such as the World War 2 Enigma code); they all need both encryption and
decryption keys (sometimes identical).</p>
<p>In some cases (such as the Hill cipher), the key is represented by a matrix.</p>
<p>You have to carry out such a matrix-based ciphering software, using the following process to encrypt :</p>

   - Transcript the key into numbers using the ASCII table,
   - Convert the numbered key into a square matrix, the smallest possible size, and filling the lines first,
   - Transcript the clear message into numbers using the ASCII table,
   - Convert the numbered message into a matrix; its number of columns should fit the key matrix size, and its number of lines should be as small as possible,
   - Multiply the 2 matrices, and write the answer linearly to get the encrypted message.

<h2> Usage </h2>

![image](https://user-images.githubusercontent.com/91891487/182238991-c5509f9a-3074-4d21-8e2b-bbedad9c2a79.png)

<h2> Example </h2>

![image](https://user-images.githubusercontent.com/91891487/182239434-2adb20d6-b675-4650-b90b-bd1cd4272c4f.png)

![image](https://user-images.githubusercontent.com/91891487/182239664-e2ff37d6-ebda-47b2-aa52-074ed8c5baea.png)
