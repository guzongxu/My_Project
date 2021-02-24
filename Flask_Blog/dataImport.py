import json

from flaskblog import db
from flaskblog.models import Post, User

f = open("posts.json", encoding="utf-8")
# 1.将数据导入程序
data = json.load(f)
# 2.遍历data，打印列表中的每一个字典
for dict_data in data:
    # print(dict_data)
    # print(dict_data['title'])
    # print(dict_data['content'])
    id = dict_data["user_id"]
    # user('guzongxu', 'gzx723547242@gmail.com', '8916f94bf72e49c7.jpg')
    # user = User.query.get(id)
    # user = User.query.filter_by(username='guzongxu').first()

    # new_post = Post(title=dict_data['title'], content=dict_data['content'], author=user)
    # db.session.add(new_post)
    # db.session.commit()
