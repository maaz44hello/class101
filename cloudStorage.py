import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token = 'sl.BIBtLPQFzj3scIPmQdNZt0_9q8_58BG9GPzKdhz-yHm99JNMPggbOWM8MVVjfEFUn1KuZIx66yuiZjhWEBj-NB_wAOF4M5DhSRlHhArLuwPtOfchN8_aI82gjDomJOILjkZp_EU'            
    transferData = TransferData(access_token)
    
    file_from  = input("Enter The File Path To Transfer:")
    file_to = input("Enter The Full Path To Upload To DropBox:")

    # API v2
    transferData.upload_file(file_from,file_to)
    print("File has been moved") 

main()



