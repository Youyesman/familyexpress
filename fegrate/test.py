def post_form(request, id=0):
    
        if request.method == "GET":
            if id == 0:
                form = PostForm()
            else:
                post = Post.objects.get(pk=id)
                form = PostForm(instance=post)
            return render(request, "feg/post_form.html", {'form': form})
        else:
            if id == 0:
                form = PostForm(request.POST)
            else:
                post = Post.objects.get(pk=id)
                form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form = form.save(commit=False)
                user_id = request.user.pk
                form.username = User.objects.get(pk=user_id)
                form.save()
            return redirect('/feg/post_list.html')
