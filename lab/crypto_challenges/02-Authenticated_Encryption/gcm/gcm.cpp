#include <iostream> 
#include <string>
#include <stdio.h> // for fopen(), etc.
#include <limits.h> // for INT_MAX
#include <string.h> // for memset()
#include <openssl/evp.h>
#include <openssl/pem.h>
#include <openssl/rand.h>
using namespace std;

int handleErrors(){
	printf("An error occourred.\n");
	exit(1);
}

// The function returns the ciphertext lenght
int gcm_encrypt(unsigned char *plaintext, int plaintext_len,
                unsigned char *aad, int aad_len,
                unsigned char *key,
                unsigned char *iv, int iv_len,
                unsigned char *ciphertext,
                unsigned char *tag)
{
    // write the body
}

// The function returns the plaintext lenght, if it completes successfully,
//  -1 otherwise
int gcm_decrypt(unsigned char *ciphertext, int ciphertext_len,
                unsigned char *aad, int aad_len,
                unsigned char *tag,
                unsigned char *key,
                unsigned char *iv, int iv_len,
                unsigned char *plaintext)
{
    // write the body
}

int main (void)
{
	unsigned char msg[] = "Short message";
	//create key
	unsigned char key_gcm[]="1234567890123456";
	unsigned char iv_gcm[]= "123456780912";
	unsigned char *cphr_buf;
	unsigned char *tag_buf;
	int cphr_len; // ciphertext lenght
	int tag_len; // tag lenght
	int pt_len; // plaintext lenght
	// size the plaintext buffer lenght 
	// pt_len = ???;
	cphr_buf=(unsigned char*)malloc(pt_len);
	tag_buf=(unsigned char*)malloc(16);
	gcm_encrypt(msg, pt_len, iv_gcm, 12, key_gcm, iv_gcm, 12, cphr_buf, tag_buf);
	cout<<"CT:"<<endl;
	BIO_dump_fp (stdout, (const char *)cphr_buf, pt_len);
	cout<<"Tag:"<<endl;
	BIO_dump_fp (stdout, (const char *)tag_buf, 16);
	unsigned char *dec_buf; // pointer to the decryption buffer
	// allocated the decryption buffer
	// dec_buf=(unsigned char*)malloc(pt_len);
	gcm_decrypt(cphr_buf, pt_len, iv_gcm, 12, tag_buf, key_gcm, iv_gcm, 12, dec_buf);
	cout<<"PT:"<<endl;
	BIO_dump_fp (stdout, (const char *)dec_buf, pt_len);
	return 0;
}
