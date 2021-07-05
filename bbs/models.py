from django.db import models

class Topic(models.Model):

    class Meta:
        db_table = "topic"

    comment     = models.CharField(verbose_name="コメント",max_length=2000)
    attachment  = models.FileField(verbose_name="添付ファイル",upload_to="file/",default="",blank=True)
    mime        = models.TextField(verbose_name="MIMEタイプ",default="",blank=True)

    def __str__(self):
        return self.comment


#リプライ用のモデルクラス(テーブル)
class TopicReply(models.Model):

    class Meta:
        db_table = "topic_reply"

    comment     = models.CharField(verbose_name="コメント",max_length=2000)
    attachment  = models.FileField(verbose_name="添付ファイル",upload_to="file/",default="",blank=True)
    mime        = models.TextField(verbose_name="MIMEタイプ",default="",blank=True)

    #1対多のリレーションを作るにはForeignKeyを使う。(1に当たるモデルクラスを指定、削除されたときの挙動を示すフィールドオプションのon_deleteは指定必須)
    #models.CASCADEでトピックが消された時、そのトピックへのリプライも全て削除する
    target      = models.ForeignKey(Topic,verbose_name="リプライ対象のトピック",on_delete=models.CASCADE)

    def __str__(self):
        return self.comment


