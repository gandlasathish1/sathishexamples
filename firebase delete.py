from firebase.firebase import FirebaseApplication
fire=FirebaseApplication("https://marchent-project-c7c4f.firebaseio.com/marchent",None)
pno=int(input("Enter product no:"))
fire.delete("stock",pno)
print("product deleted")