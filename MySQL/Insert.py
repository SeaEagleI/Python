#coding:utf-8
import pymysql
import time
from Search import search

conn = pymysql.connect(host='localhost',user='root',
        passwd='123',charset='utf8')
cursor = conn.cursor()
db_name = "Library"
tb_name = "wordlist"
hint = "We provide with extraodinary experiences and \
      \nquick access to insert,motify,sort,drop or search\
      \nyour word(s) in MySQL.And each of your operations\
      \nwill be recorded as well.\
      \nRespectively,'q','m','d','s' stand for the \
      \noperations mentioned above."
shift = "\033[C\033[1A\r"
turns = 100

def show(list):
    print("id:              {}".format(list[0]))
    print("terms:           {}".format(list[1]))
    means = eval(list[2])
    for i in range(len(means)):
        if i==0:
            print("translations:    {}".format(means[i]))
        else:
            print("{}{}".format(' '*17,means[i]))
    print("insert time:     {:^10}".format(list[3]))
    if list[4]==None:
        print("content:         {:^10}".format("None"))
    else:
        print("content:         {:^10}".format(list[4]))
 
def Display(word):
    count = cursor.execute('select * from '+ tb_name)
    print('Number of items: {}'.format(count))
    cursor.execute("select * from wordlist where terms='"+word+"'")
    try:
        result = cursor.fetchall()[0]
        show(result)
    except:
        print("Not Found")
    pass

def Insert(word):
    conn.select_db(db_name)
    means = str(search(word))
    time_t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    sql = "insert into wordlist values(null,\'"+word+"\',\""+means+"\",\'"+time_t+"\',null)"
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()

def Delete(word):
    conn.select_db(db_name)
    initial = cursor.execute('select * from '+ tb_name)
    sql = "delete from "+tb_name+" where terms=\'"+word+"\'"
    try:
        cursor.execute(sql)
        conn.commit()
        end = cursor.execute('select * from '+ tb_name)
        if initial>end:
            _del = initial-end
            print("Successfully deleted {} words".format(_del))
        else:
            print("Not Found")
            _del = 0
        print('Rest of items:{}'.format(end))
        return _del
    except:
        conn.rollback()
    
def Search(key):
    conn.select_db(db_name)
    sql = "select * from "+tb_name+" where terms like \'"+key+"\'"
    try:
        count = cursor.execute(sql)
    except:
        print("Failure")
        return
    print('Items related to:{}'.format(count))
    rows = cursor.fetchall()
    print('-----------------------------------')
    for row in rows:
        print("{:^3} {:^10} {:^50} {:^19} {}".format(row[0],row[1],row[2],row[3],row[4]))
    return count

def main():
    print(hint+'\n')
    _del,_sea,_ins = 0,0,0
    for i in range(turns):
        word = input("Insert ["+str(i+1)+"]:")
        #start = time.perf_counter()
        if word=="q":
            print("{} inserted, {} searched and {} deleted.".format(_ins,_sea,_del))
            break
        elif word=="d":
            word = input(shift+"Delete ["+str(i+1)+"]: ")
            _del += Delete(word)
            print("")
        elif word=="s":
            key = input(shift+"Search ["+str(i+1)+"]: ")
            _sea += Search(key)
            print("")
        else:
            Insert(word)
            _ins += 1
            print("Display["+str(i+1)+"]:")
            Display(word)
            #print("(Time used in {:^.4}s)".format(time.perf_counter()-start))
            print("")
    
main()

