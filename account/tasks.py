from django.core.mail import send_mail
from decouple import config
from celery import shared_task


@shared_task
def send_activation_code(email: str, code: str):
	message = ""
	html = f"""
<h1>для активации нажмите на кнопку</h1>
<a href="{config('LINK')}api/v1/account/activate/{code}">
<button>Activate</button>
</a>
"""
	send_mail(
		subject="Активация аккаунта",
		message=message,
		from_email="a@gmail.com",
		recipient_list=[email],
		html_message=html
	)

@shared_task
def send_confirmation(email):
  message = ""
  html = f"""
<h1>Вы успешно зарегистрировались!</h1>
<br>
<br>
<img src="https://res.cloudinary.com/teepublic/image/private/s--IhL5TJpc--/c_crop,x_10,y_10/c_fit,h_1109/c_crop,g_north_west,h_1260,w_1050,x_-125,y_-76/co_rgb:000000,e_colorize,u_Misc:One%20Pixel%20Gray/c_scale,g_north_west,h_1260,w_1050/fl_layer_apply,g_north_west,x_-125,y_-76/bo_140px_solid_white/e_overlay,fl_layer_apply,h_1260,l_Misc:Art%20Print%20Bumpmap,w_1050/e_shadow,x_6,y_6/c_limit,h_1254,w_1254/c_lpad,g_center,h_1260,w_1260/b_rgb:eeeeee/c_limit,f_auto,h_630,q_90,w_630/v1670208028/production/designs/37158337_0.jpg" alt="ghbdtn">
"""
  send_mail(
    subject="Подтверждение регистрации",
    message=message,
    from_email="a@gmail.com",
    recipient_list=[email],
    html_message=html
  )
