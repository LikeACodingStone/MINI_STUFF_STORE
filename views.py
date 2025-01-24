from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect

@login_required
@user_passes_test(lambda u: u.is_staff)
def admin_dashboard(request):
    # 添加文件大小限制
    if request.FILES['image'].size > 5 * 1024 * 1024:  # 5MB
        messages.error(request, '文件太大')
        return redirect('admin_dashboard') 