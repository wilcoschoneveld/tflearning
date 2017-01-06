import tensorflow as tf


# Create two matrices
matrix1 = tf.constant([[3, 3]])
matrix2 = tf.constant([[2], [1]])

# Multiply two matrices
product = tf.matmul(matrix1, matrix2)

# Run the graph in a session
with tf.Session() as sess:
    result = sess.run(product)
    print(result)
