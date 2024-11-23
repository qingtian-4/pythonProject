from email.mime.text import MIMEText
import smtplib

# 构建邮件内容
msg = MIMEText('牢超，我测试个东西', 'plain', 'utf-8')
msg['Subject'] = "测试邮件"
msg['From'] = '3115922568@qq.com'
msg['To'] = '2829483441@qq.com'

# 输入Email地址和口令（不是密码，而是授权码）:
from_addr = '3115922568@qq.com'
password = 'itiwfijemgflddfd' # 每次都要重新更换授权码
# 输入收件人地址:
to_addr = '2829483441@qq.com'
# 输入SMTP服务器地址:
smtp_server = 'smtp.qq.com'

# 使用 SMTP_SSL 连接
server = smtplib.SMTP_SSL(smtp_server, 465)  # 使用 SSL 的 465 端口
server.set_debuglevel(1)
try:
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    print("邮件发送成功")
except Exception as e:
    print(f"邮件发送失败: {e}")
finally:
    server.quit()
