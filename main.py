import eel
import vk_api


@eel.expose
def signUp(login, password):
    if (login != '' and password != ''):
        user = [login, password]
    return user


@eel.expose
def signUpVK(login, password):
    if (login != '' and password != ''):
        vk_session = vk_api.VkApi(login, password)
    vk_session.auth()
    vk = vk_session.get_api()
    user = vk.users.get()
    return user


eel.init('web')
eel.start('main.html', size=(500, 500))
