

#　本のコードでは作れない
import datetime

file = open('0804/hoge.txt', 'w', encoding='UTF-8')
file.write(str(datetime.datetime.now()) + '\n')
file.close()
print('ファイルを保存しました。')


# ネットでのコードの書き方だと作れる。
faile = open('test.txt', 'w', encoding='utf-8')
faile.write('1:テストです\n')
faile.close()
print("ファイルを保存しました。")