### Aes-1

![Aes-1](https://github.com/Hed6eH0g/ctf/blob/main/2023/n00bzctf/crypto/aes-1/aes-1_0.png)

Though AES in this challenge looks adopting a salt, it does not choose at random.
It means that we can easily obtain the same key by just running the program, and threrefore, just implimenting the decryption and running it with `javac {AESChallenge.java}` and `java AESChallenge` allow us to have the flag.
The entire codes are as follows:
```
import javax.crypto.Cipher;
import javax.crypto.SecretKey;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.PBEKeySpec;
import javax.crypto.spec.SecretKeySpec;
import java.nio.charset.StandardCharsets;
import java.security.spec.KeySpec;
import java.util.Base64;

public class AESChallenge {
    private static final String AES_ALGORITHM = "AES";
    private static final String PBKDF2_ALGORITHM = "PBKDF2WithHmacSHA256";
    private static final int ITERATIONS = 10000;
    private static final int KEY_SIZE = 256;

    private static SecretKey generateKey(String password, byte[] salt) throws Exception {
        KeySpec spec = new PBEKeySpec(password.toCharArray(), salt, ITERATIONS, KEY_SIZE);
        SecretKeyFactory factory = SecretKeyFactory.getInstance(PBKDF2_ALGORITHM);
        SecretKey tmp = factory.generateSecret(spec);
        return new SecretKeySpec(tmp.getEncoded(), AES_ALGORITHM);
    }

    private static String encrypt(String plainText, SecretKey key) throws Exception {
        Cipher cipher = Cipher.getInstance(AES_ALGORITHM);
        cipher.init(Cipher.ENCRYPT_MODE, key);
        byte[] encryptedBytes = cipher.doFinal(plainText.getBytes(StandardCharsets.UTF_8));
        return Base64.getEncoder().encodeToString(encryptedBytes);
    }

    private static String decrypt(String cipherText, SecretKey key) throws Exception {
        Cipher decrypter = Cipher.getInstance(AES_ALGORITHM);
        decrypter.init(Cipher.DECRYPT_MODE, key);
        byte[] c = Base64.getDecoder().decode(cipherText); 
        String text = new String(decrypter.doFinal(c));
        return text;
    }

    public static void main(String[] args) {
        String flag = "REDACTED";
        String password = "aesiseasy";
        byte[] salt = "saltval".getBytes(StandardCharsets.UTF_8);

        try {
            SecretKey key = generateKey(password, salt);
            System.out.println("Key           : " + key);
            // String encryptedFlag = encrypt(flag, key);
            String encryptedFlag = "FOqxc90aMQZydCQb2MUm5tj4kRIxxVeCDWzAANfOrr8JItHYneUHhSV0awvQIo/8E1LtfYm/+VVWz0PDK6MXp38BWHoFDorhdS44DzYj9CQ=";
            System.out.println("Encrypted Flag: " + encryptedFlag);
            String Flag = decrypt(encryptedFlag, key);
            System.out.println("Flag          : " + Flag);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```