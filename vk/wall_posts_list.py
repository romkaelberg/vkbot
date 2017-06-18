#Парсер постов со стены пользователя
def wall_posts_list(posts,number_of_posts):
    print("| WALL POSTS LIST ")
    for i in range(number_of_posts):
        if i > 0:
            if(posts[i]['text'] != ""):
                print("|-----------------------------------------------")
                print("| POST: " + posts[i]['text'])
                print("| LIKES: " + str(posts[i]['likes']['count']))
            else:
                print("|-----------------------------------------------")
                print("| POST: " + "NO TEXT!!!")
                print("| LIKES: " + str(posts[i]['likes']['count']))
            if(i == number_of_posts - 1):
                print("|-----------------------------------------------")
                print("\n")