#include <openssl/conf.h>
#include <openssl/evp.h>
#include <openssl/err.h>
#include <string.h>

void handleErrors(void)
{
  ERR_print_errors_fp(stderr);
  abort();
}

int encrypt(unsigned char *plaintext, int plaintext_len, unsigned char *key,
            unsigned char *iv, unsigned char *ciphertext)
{
  EVP_CIPHER_CTX *ctx;

  int len;
  int ciphertext_len;

  /* Create and initialise the context */
  ctx = EVP_CIPHER_CTX_new();

  // Encrypt init
  EVP_EncryptInit_ex(ctx, EVP_aes_128_ecb(), NULL, key, iv);

  // Encrypt Update: one call is enough because our mesage is very short.
  EVP_EncryptUpdate(ctx, ciphertext, &len, plaintext, plaintext_len);
  ciphertext_len = len;

  // Encrypt Final. Finalize the encryption and adds the padding
  EVP_EncryptFinal(ctx, ciphertext + len, &len);
  ciphertext_len += len;

  // MUST ALWAYS BE CALLED!!!!!!!!!!
  EVP_CIPHER_CTX_free(ctx);

  return ciphertext_len;
}

int decrypt(/*Think about what you need!*/ unsigned char *ciphertext, int ciphertext_len, unsigned char *key,
            unsigned char *iv, unsigned char *plaintext)
{
  // do stuff
  EVP_CIPHER_CTX *ctx;

  int len;
  int plaintext_len;

  ctx = EVP_CIPHER_CTX_new();
  EVP_DecryptInit(ctx, EVP_aes_128_ecb(), key, iv);

  if (1 != EVP_DecryptUpdate(ctx, plaintext, &len, ciphertext, ciphertext_len))
    handleErrors();
  plaintext_len = len;

  if (1 != EVP_DecryptFinal(ctx, plaintext + len, &len))
    handleErrors();
  plaintext_len += len;

  EVP_CIPHER_CTX_free(ctx);

  return plaintext_len;
}

int main(void)
{
  // 128 bit key (16 characters * 8 bit)
  unsigned char *key = (unsigned char *)"0123456789012345";

  // Our Plaintext
  unsigned char plaintext[] = "The World Is Smaller Than You Think";

  /* Buffer for ciphertext. Ensure the buffer is long enough for the
   * ciphertext which may be longer than the plaintext, depending on the
   * algorithm and mode*/
  unsigned char *ciphertext = (unsigned char *)malloc(strlen((char *)plaintext) + EVP_MAX_BLOCK_LENGTH);

  // unsigned char *ciphertext = (unsigned char *)malloc(sizeof(plaintext) + 32);

  int decryptedtext_len, ciphertext_len;
  // Encrypt utility function
  ciphertext_len = encrypt(plaintext, strlen((char *)plaintext), key, NULL, ciphertext);

  // Redirect our ciphertext to the terminal
  printf("Ciphertext is:\n");
  BIO_dump_fp(stdout, (const char *)ciphertext, ciphertext_len);

  // Buffer for the decrypted text
  // unsigned char *decryptedtext = (unsigned char *)malloc(sizeof(ciphertext));
  unsigned char *decryptedtext = (unsigned char *)malloc(ciphertext_len);

  // Decrypt the ciphertext
  decryptedtext_len = decrypt(ciphertext, ciphertext_len, key, NULL, decryptedtext);

  // Null-terminate the decrypted text
  decryptedtext[decryptedtext_len] = '\0';

  // Show the decrypted text
  printf("Decrypted text is:\n");
  printf("%s\n", decryptedtext);

  return 0;
}
