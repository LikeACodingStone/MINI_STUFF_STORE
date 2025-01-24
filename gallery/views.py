from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm, ImageUploadForm
from .models import Category, Image
from .storage import QiniuStorage
from .utils import compress_image

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('gallery_view')
    else:
        form = UserRegistrationForm()
    return render(request, 'gallery/register.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_staff)
def admin_dashboard(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            
            # 压缩图片
            file = request.FILES['image']
            compressed_image = compress_image(
                file,
                max_size=(800, 800),  # 最大尺寸
                quality=85  # 压缩质量
            )
            
            # 上传到七牛云
            storage = QiniuStorage()
            filename = f"images/{file.name}"
            image_url = storage.upload_image(compressed_image, filename)
            
            if image_url:
                image.image_url = image_url
                image.uploaded_by = request.user
                image.save()
                
            return redirect('admin_dashboard')
    else:
        form = ImageUploadForm()
    
    categories = Category.objects.all()
    images = Image.objects.all()
    return render(request, 'gallery/admin_dashboard.html', {
        'form': form,
        'categories': categories,
        'images': images
    })

@login_required
def gallery_view(request):
    categories = Category.objects.all()
    selected_category = request.GET.get('category')
    
    if selected_category:
        images = Image.objects.filter(category_id=selected_category)
    else:
        images = Image.objects.all()
        
    return render(request, 'gallery/gallery_view.html', {
        'categories': categories,
        'images': images
    }) 