# RSA Algorithm Implementation

A Command Line Interface (CLI) application that demonstrates the implementation of the RSA (Rivest-Shamir-Adleman) cryptographic algorithm for educational and practical purposes.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Algorithm Explanation](#algorithm-explanation)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Examples](#examples)
- [Security Considerations](#security-considerations)
- [Contributing](#contributing)
- [License](#license)

## 🔍 Overview

RSA is one of the most widely used public-key cryptographic algorithms. This implementation provides a practical demonstration of how RSA encryption and decryption works, making it perfect for educational purposes and understanding the fundamentals of asymmetric cryptography.

### Key Features
- ✅ Pure implementation with no external dependencies
- 🖥️ Command-line interface for easy interaction
- 🔐 Complete RSA key generation, encryption, and decryption
- 📚 Educational code structure with clear documentation
- 🚀 Ready to run out of the box

## 🛠️ Features

- **Key Generation**: Generate RSA public and private key pairs
- **Encryption**: Encrypt messages using the public key
- **Decryption**: Decrypt messages using the private key
- **CLI Interface**: User-friendly command-line interaction
- **No Dependencies**: Built using only standard libraries

## 🔢 Algorithm Explanation

The RSA algorithm is based on the mathematical difficulty of factoring large composite numbers. Here's how it works:

### Key Generation
1. **Choose two distinct prime numbers** p and q
2. **Compute n = p × q** (modulus for both keys)
3. **Calculate φ(n) = (p-1)(q-1)** (Euler's totient function)
4. **Choose e** such that 1 < e < φ(n) and gcd(e, φ(n)) = 1
5. **Calculate d** such that d × e ≡ 1 (mod φ(n))

### Public Key: (n, e)
### Private Key: (n, d)

### Encryption
- Ciphertext = (Plaintext^e) mod n

### Decryption  
- Plaintext = (Ciphertext^d) mod n

## 🚀 Installation

### Prerequisites
- A C/C++ compiler (GCC recommended) or appropriate IDE
- No additional libraries required

### Steps
1. **Clone the repository**
   ```bash
   git clone https://github.com/vehutech/rsa_algorithm.git
   ```

2. **Navigate to the project directory**
   ```bash
   cd rsa_algorithm
   ```

3. **Compile the code**
   ```bash
   gcc -o rsa_algorithm main.c
   ```
   *Note: Adjust the compilation command based on your specific files*

4. **Run the application**
   ```bash
   ./rsa_algorithm
   ```

### Alternative: Using an IDE
1. Download or clone the repository
2. Open the project in your preferred IDE (Code::Blocks, Visual Studio, etc.)
3. Compile and run directly from the IDE

## 💻 Usage

### Running the Application
```bash
./rsa_algorithm
```

The application will present you with a menu-driven interface where you can:

1. **Generate RSA Key Pair**
   - Creates public and private keys
   - Displays the generated keys

2. **Encrypt a Message**
   - Input your plaintext message
   - Uses the public key for encryption
   - Shows the encrypted ciphertext

3. **Decrypt a Message**
   - Input the ciphertext
   - Uses the private key for decryption
   - Displays the original message

## 📁 Project Structure

```
rsa_algorithm/
├── README.md
├── main.c                 # Main program file
├── rsa.c                  # RSA algorithm implementation
├── rsa.h                  # Header file with declarations
├── utils.c                # Utility functions
├── utils.h                # Utility function headers
└── examples/              # Example inputs and outputs
```

*Note: Actual file structure may vary. Please check the repository for exact files.*

## ⚙️ How It Works

### 1. Key Generation Process
- Generates random prime numbers
- Calculates the public and private key components
- Ensures mathematical validity of the key pair

### 2. Encryption Process
- Takes plaintext input from user
- Applies RSA encryption formula
- Returns encrypted ciphertext

### 3. Decryption Process
- Takes ciphertext as input
- Applies RSA decryption formula using private key
- Recovers original plaintext message

## 📝 Examples

### Example 1: Basic Encryption/Decryption
```
1. Generate Keys
   Public Key: (n=3233, e=17)
   Private Key: (n=3233, d=413)

2. Encrypt "HELLO"
   Input: "HELLO"
   Output: [encrypted_values]

3. Decrypt
   Input: [encrypted_values]
   Output: "HELLO"
```

### Example 2: Numerical Example
```
Plaintext: 123
Public Key: (n=3233, e=17)
Ciphertext: 123^17 mod 3233 = 855

Decryption: 855^413 mod 3233 = 123
```

## 🔒 Security Considerations

### Educational Purpose
⚠️ **Important**: This implementation is designed for educational purposes and may not be suitable for production use without additional security measures.

### Security Notes
- **Key Size**: Use larger prime numbers for real-world applications
- **Random Number Generation**: Ensure cryptographically secure randomness
- **Padding**: Consider implementing OAEP or PKCS#1 padding
- **Side-Channel Attacks**: Production implementations should protect against timing attacks

### Best Practices
- Never reuse keys across different applications
- Keep private keys secure and encrypted
- Use appropriate key sizes (2048-bit minimum for real applications)
- Implement proper error handling and validation

## 🤝 Contributing

We welcome contributions to improve this educational RSA implementation!

### How to Contribute
1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**
4. **Test thoroughly**
5. **Commit your changes**
   ```bash
   git commit -m "Add: your feature description"
   ```
6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```
7. **Create a Pull Request**

### Areas for Contribution
- Code optimization and cleanup
- Additional security features
- Enhanced user interface
- More comprehensive examples
- Documentation improvements
- Test cases and validation

## 📄 License

This project is open source. Please check the repository for specific license information.

## 🙏 Acknowledgments

- RSA algorithm inventors: Rivest, Shamir, and Adleman
- Contributors to this educational implementation
- The open-source community for cryptographic education resources

## 📚 Additional Resources

### Learn More About RSA
- [RSA Algorithm on Wikipedia](https://en.wikipedia.org/wiki/RSA_(cryptosystem))
- [Introduction to Modern Cryptography](https://www.cryptography.io/)
- [Cryptographic Engineering](https://cryptoengineering.com/)

### Related Topics
- Public Key Cryptography
- Prime Number Generation
- Modular Arithmetic
- Cryptographic Security

---

**Note**: This implementation is for educational purposes. For production cryptographic needs, please use established cryptographic libraries and consult with security experts.

---

*Made with ❤️ for cryptography education*
