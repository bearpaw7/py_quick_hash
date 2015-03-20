# py_quick_hash
Hash files using "hashlib" from Python 2.7 standard library. Works on files of any(?) size or content.

Example 0:
> python.exe hash.py python.exe

Output 0:

        Hash    python.exe
        MD5     4976fd068f84daf688a1028366e77516
        SHA256  808df699747cf68d4c8def86a930cadfc92a06b6e10d0cafb68d9eb4c355015f
        SHA512  15c62f0ccb42af936d19f9e572beacf1dfe4b7e49dfc468cf9c3bfa607b4dcfb473d6f38c63f0ca76e4c29f20bf9e7d3c2f50e587dd95eb8f43659ec08275b4f


Example 1:
> python.exe hash.py LICENSE.txt NEWS.txt README.txt python.exe pythonw.exe

Output 1:

        Hash    LICENSE.txt
        MD5     59252a487e72a43ad3b65dd6e4562b79
        SHA256  50e2003e5f83c7223fb446f18450a8db025237ac3bda84e4a2ead065acfcee16
        SHA512  d4d9ba4f16c3ec22217e5be47303b4f3fd816a86cd2c5194e95a876f8c7f7ffac06a6e76e1a39644c38be63fbac0cfc3d67e1ce0a71aca96aa05889f6b671a11

        Hash    NEWS.txt
        MD5     3bac1d1574833850fda4af408edaf54c
        SHA256  4dcc0b7690abed675db4bc2306491ac04be35547e4014cd60f120ac3ec7d402b
        SHA512  0bfcea52cf6e86bbe0a0d72755acf2f5e47371d6219c4e31f71fe99080ebd93b8dfff1b90148c1fb448c1d3cb99600d467ffeadbc23051ead03b1631c0bc486e

        Hash    README.txt
        MD5     a98002086c90bde9a53c2195f0b82d3e
        SHA256  f94358f73c606eaccc7930cfc7011a889ed82aad588f20457e045cda607ae3b7
        SHA512  e3343648a525a1f660f7ddf43108379dffdf3afcccd0b074c7b9fb98839e941c8ac7986427e7e4eeab63ccd9dca9534175cb0acbd3d6949138a758ae496c810c

        Hash    python.exe
        MD5     4976fd068f84daf688a1028366e77516
        SHA256  808df699747cf68d4c8def86a930cadfc92a06b6e10d0cafb68d9eb4c355015f
        SHA512  15c62f0ccb42af936d19f9e572beacf1dfe4b7e49dfc468cf9c3bfa607b4dcfb473d6f38c63f0ca76e4c29f20bf9e7d3c2f50e587dd95eb8f43659ec08275b4f

        Hash    pythonw.exe
        MD5     8742cd2d534883b4320efc118007aa32
        SHA256  0264ee0da2d29dbffae3084bf5852e880d9d26f8de0936281e0566827c2950e1
        SHA512  c2633b9bc16bac3d6b0398832abee3ebbc4a597388c7275d02d1d17db5ce61717b61c5f3e3cea67f7b106a79e0d22dde873a43d1746010c232ba1e18081a8045

Example 2:
> python.exe hash.py e:\e_downloads\debian-7.8.0-amd64-DVD-1.iso

Output 2:

        Hash    e:\e_downloads\debian-7.8.0-amd64-DVD-1.iso
        MD5     601377b0a66c2629dff24a1a53271bd8
        SHA256  64b3db0898bbf1cf42ff3f000965acddd126b79967b671cf04b2c5536814ec43
        SHA512  9dd46c7a8fdfee3510d8e5107f6c7f7a8859c21754b0446e2638a08b0b2bbfa9cc543dcf3a16d02b1ef4b69faf7fa58ff9970ea9ddf6608b1bf3e25019d72a9e

fin
