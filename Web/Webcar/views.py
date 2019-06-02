from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Webcar import models


# Create your views here.


def logins(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        联系电话 = request.POST.get('联系电话')
        用户密码 = request.POST.get('用户密码')
        # user_obj = models.Users.objects.filter(联系电话=联系电话, 用户密码=用户密码).first()
        user = authenticate(request,username=request.POST['联系电话'],password=request.POST['用户密码'])
        if user:
            # if user_obj:
                login(request,user)
                return redirect('主界面')
        else:
            return HttpResponse('联系电话或密码错误')


def logouts(request):
    logout(request)
    return redirect('主界面')


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        联系电话 = request.POST.get('联系电话')
        用户密码 = request.POST.get('用户密码')
        确认密码 = request.POST.get('确认密码')
        if 联系电话 and 用户密码 and 确认密码:
            if 用户密码 == 确认密码:
                user_obj = models.Users.objects.filter(联系电话=联系电话).first()
                if user_obj:
                    return HttpResponse('该号码已注册')
                else:
                    User.objects.create_user(username=联系电话,password=用户密码).save()
                    models.Users.objects.create(联系电话=联系电话, 用户密码=用户密码).save()
                    return redirect('登录')
            else:
                return HttpResponse('两次密码不一致！！')
        else:
            return HttpResponse('老哥要填的已经够少了，你就别空了把>.<')



@login_required(login_url='登录')
def personalcenter(request):
    userid = User.objects.get(username=request.user.username)
    user_obj = models.Users.objects.filter(联系电话=userid).first()
    if user_obj:
        informations = {'anothername':user_obj.账号,'groupname':user_obj.集团名,'names':user_obj.用户姓名,'carnumber':user_obj.车牌号,'phone':user_obj.联系电话,'emial':user_obj.邮箱}
        return render(request, 'personalcenter.html',informations)


@login_required(login_url='登录')
def editpersonal(request):
    if request.method == 'GET':
        userid = User.objects.get(username=request.user.username)
        user_obj = models.Users.objects.filter(联系电话=userid).first()
        if user_obj:
            informations = {'anothername': user_obj.账号, 'names': user_obj.用户姓名,'carnumber': user_obj.车牌号,
                            'phone': user_obj.联系电话, 'emial': user_obj.邮箱}
            return render(request, 'editpersonal.html', informations)
    else:
        账号 =request.POST.get('账号')
        用户姓名 = request.POST.get('用户姓名')
        联系电话 = request.POST.get('联系电话')
        邮箱 = request.POST.get('邮箱')
        车牌号 = request.POST.get('车牌号')
        userid = User.objects.get(username=request.user.username)
        user_obj = models.Users.objects.filter(联系电话=userid).first()
        if user_obj:
            User.objects.filter(username=userid).update(username=联系电话)
            models.Users.objects.filter(联系电话=userid).update(账号=账号,用户姓名=用户姓名,联系电话=联系电话,
                                                            邮箱=邮箱,车牌号=车牌号 )
        return redirect('个人信息')


@login_required(login_url='登录')
def dashboard(request):
    userid = User.objects.get(username=request.user.username)
    user_obj = models.Users.objects.filter(联系电话=userid).first()
    if user_obj:
        informations = {'credit':user_obj.信用分值}
        return render(request, 'dashboard.html',informations)



def main(request):
    if request.method == 'GET':
        return render(request, 'main.html')


def editpassword(request):
    if request.method == 'GET':
        return render(request, 'editpassword.html')
    else:
        联系电话 = request.POST.get('联系电话')
        旧密码 = request.POST.get('密码')
        新密码 = request.POST.get('用户密码')
        确认密码 = request.POST.get('确认密码')
        user_obj = models.Users.objects.filter(联系电话=联系电话).first()
        if 联系电话 and 旧密码 and 新密码 and 确认密码:
            if user_obj:
                if user_obj.用户密码 == 旧密码:
                    if 新密码 == 确认密码:
                        User.objects.filter(username=联系电话).delete()
                        User.objects.create_user(username=联系电话, password=新密码).save()
                        models.Users.objects.filter(联系电话=联系电话).update(用户密码=新密码)
                        return redirect('登录')
                    else:
                        return HttpResponse('两次密码不一致！！')
                else:
                    return HttpResponse('旧密码输入错误请确认大小写!!')
            else:
                return HttpResponse('该联系电话未注册或您输入的号码有误')
        else:
            return HttpResponse('都是必填选项，请一个也不要放过')


@login_required(login_url='登录')
def order(request):
    if request.method == 'GET':
        order_obj = models.Orders.objects.filter(联系电话=request.user.username).first()
        if order_obj:
            informations = {'starttime': order_obj.充电开始时间, 'ordernum': order_obj.订单号, 'pilenum': order_obj.电桩编号,
                            'actiontypenum': order_obj.充电行为类型编号, 'credit': order_obj.订单分值小计}
            return render(request, 'order.html', informations)
        else:
            return HttpResponse('您还没有下过订单哦，下过单以后才能在这里查看哦！！')


@login_required(login_url='登录')
def subscribe(request):
    if request.method == 'GET':
        if request.method == 'GET':
            sub_obj = models.Subs.objects.filter(联系电话=request.user.username).first()
            if sub_obj:
                informations = {'starttime': sub_obj.预约充电开始时间, 'ordernum': sub_obj.预约号, 'pilenum': sub_obj.电桩编号,
                                'actiontypenum': sub_obj.预约状态, 'credit': sub_obj.预约分值小计}
                return render(request, 'subscribe.html',informations)
            else:
                return HttpResponse('您还没有下过预约哦，下过单以后才能在这里查看哦！！')