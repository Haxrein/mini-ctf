# Mini CTF
5 adet sorudan oluşan geliştirilebilir bir mini CTF platformu.


# Özellikleri

Tüm soruların çözülmesinin ardından yarışmacılara üstünde isimlerinin yazılı olduğu sertifika verme imkanı.
Admin paneli ile sisteme kayıtlı kullanıcıları görebilirsiniz.

# Ne ile geliştirildi?
Python, Flask ve SQLite kullanıldı. 


# Kurulum

1) pip install -r requirements.txt
2) database.db'de kullanıcıların tutulduğu database dosyası bulunmaktadır. Başka bir table oluşturmak isterseniz createDB.py'yi düzenleyip çalıştırabilirsiniz. Eğer başka bir işlem yapmayacaksınız bu adımı geçebilirsiniz.
3) app.py içerisinde admin kullanıcı adı, şifre gibi değişkenleri düzenleyebilirsiniz.
4) Standart olarak 5 adet soru bulunmaktadır. Daha fazla soru veya varolan soruları değiştirmek isterseniz app.py'i düzenleyebilirsiniz.
5) Sırasıyla;

export FLASK_APP=app
export FLASK_ENV=development

komutlarını çalıştırıyoruz. Bu adımdan sonra Local'de gereken adımları tamamladık.

Not: İsteğe bağlı olarak Python virutalenv kullanabilirsiniz.

# Local'de çalıştırmak için

"flask run" komutu ile standart olarak http://127.0.0.1:5000/ adresinde çalıştırabilmekteyiz.

# Global'de çalıştırmak için

Eğer tüm internete açık hale getirmek istiyorsak burada bir çok alternatif mevcut.

Bu projede ben wsgi, Gunicorn ve nginx kullandım.

1) "gunicorn --bind 0.0.0.0:5000 wsgi:app" komutu ile sunucumuzu başlatıyoruz. Not: Bu adımı yapmak yerine service oluşturup da yapabilmekteyiz. Fakat ben uğraşmamak için bu yöntemi tercih ettim.
2) Ctrl+a+d ile deatch oluyoruz. (Tekrardan attach olmak için screen -r)
3) sudo nano /etc/nginx/sites-available/minictf ile nginx ayarlarını yapmamız gerekmekte.

Örnek olarak:

server {
        listen 5000;
        server_name minictf;

        access_log /var/log/nginx/minictf.access.log;
        error_log /var/log/nginx/minictf.error.log;

        location / {
                include proxy_params;
                proxy_pass http://unix:/var/www/minictf/minictf.sock;
        }
}

4) sudo ln -s /etc/nginx/sites-available/minictf /etc/nginx/sites-enabled
5) sudo systemctl restart nginx
5.1) sudo ufw delete allow 5000 (Her ihtimale karşı 5000 portunu firewall'dan izin veriyoruz)
5.2) sudo ufw allow 'Nginx Full'

Ve artık sunucumuz hazır!
