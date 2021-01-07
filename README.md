# mypkg

##ROS上で起動するpython2のプログラムです。

count.pyが最初のパブリッシャとなり、10Hｚで0からint型でカウントアップしていきます。
サブスクライバのtwice.pyで受け取ったcount.pyの値を2倍にしてtwiceという名前のパブリッシャで返します。
