from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# insert / find / update / delete

# doc = {'name':'jane','age':21}
# db.users.insert_one(doc) # users 는 collection(=db제목)

# same_ages = list(db.users.find({'age':21},{'_id':False})) # 뭔가를 users에서 찾아서 same_ages 에다가 넣음
# all = list(db.users.find({}{'_id':False}))
# for person in same_ages:
#     print(person)

#하나만 가져오기
# user = db.users.find_one({'name':'bobby'},{'_id':False})
# print(user) #제일 위에 있는 놈만 가져옴

# 업데이트
# db.users.update_one({'name':'bobby'},{'$set':{'age':28}}) #name이 bobby인 애를 찾아서 age를 19로 바꿔라
#db.users.update_many() 는 한 번에 다 바꾸는 거. 근데, 한 번에 다 바꾸는 건 너무 큰 일이기때문에 잘 안 씀

#삭제
# db.users.delete_one({'name':'bobby'})
#db.users.delete_many() 도 있는데, 이 역시 잘 안 씀

# 저장 - 예시
doc = {'name':'bobby','age':21}
db.users.insert_one(doc)

# 한 개 찾기 - 예시
user = db.users.find_one({'name':'bobby'})

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
same_ages = list(db.users.find({'age':21},{'_id':False}))

# 바꾸기 - 예시
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 지우기 - 예시
db.users.delete_one({'name':'bobby'})

