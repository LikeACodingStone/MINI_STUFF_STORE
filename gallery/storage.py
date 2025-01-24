import firebase_admin
from firebase_admin import credentials, storage
import os

class FirebaseStorage:
    def __init__(self):
        # 从环境变量获取凭证
        cred_dict = {
            "type": "service_account",
            "project_id": os.environ.get('FIREBASE_PROJECT_ID'),
            "private_key_id": os.environ.get('FIREBASE_PRIVATE_KEY_ID'),
            "private_key": os.environ.get('FIREBASE_PRIVATE_KEY').replace('\\n', '\n'),
            "client_email": os.environ.get('FIREBASE_CLIENT_EMAIL'),
            "client_id": os.environ.get('FIREBASE_CLIENT_ID'),
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": os.environ.get('FIREBASE_CLIENT_CERT_URL')
        }
        
        cred = credentials.Certificate(cred_dict)
        if not firebase_admin._apps:
            firebase_admin.initialize_app(cred, {
                'storageBucket': f"{os.environ.get('FIREBASE_PROJECT_ID')}.appspot.com"
            })
        
        self.bucket = storage.bucket()
    
    def upload_image(self, file, filename):
        blob = self.bucket.blob(filename)
        blob.upload_from_file(file)
        blob.make_public()
        return blob.public_url 