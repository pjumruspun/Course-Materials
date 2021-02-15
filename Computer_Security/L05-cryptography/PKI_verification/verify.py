from OpenSSL import crypto 
import pem

def verify(cert_path, intermediate_path):
    with open(cert_path, 'r') as cert_file:
        cert = cert_file.read()
    with open(intermediate_path, 'r') as int_cert_file: 
        int_cert = int_cert_file.read()

    pems=pem.parse_file('./ca-certificates.cert'); trusted_certs = []
    for mypem in pems:
        trusted_certs.append(str(mypem))
    trusted_certs.append(int_cert)
    verified = verify_chain_of_trust(cert, trusted_certs)
    if verified:
        print(f'Certificate {cert_path} verified')

def verify_chain_of_trust(cert_pem, trusted_cert_pems):
    certificate = crypto.load_certificate(crypto.FILETYPE_PEM, cert_pem)

    # Create and fill a X509Store with trusted certs 
    store = crypto.X509Store()
    for trusted_cert_pem in trusted_cert_pems:
        trusted_cert = crypto.load_certificate(crypto.FILETYPE_PEM, trusted_cert_pem)
        store.add_cert(trusted_cert)

    # Create a X590StoreContext with the cert and trusted certs 
    # # and verify the the chain of trust
    store_ctx = crypto.X509StoreContext(store, certificate)
    # Returns None if certificate can be validated
    result = store_ctx.verify_certificate()

    if result is None: return True
    else:
        return False

to_verify = [
    ('twitter_com.cert', 'intermediate_twitter.pem'),
    ('google_com.cert', 'intermediate_google.cert'),
    ('chula.cert', 'intermediate_chula.cert'),
]

for pair in to_verify: verify(pair[0], pair[1])