def CartSubmit(request):
    cart = Cart(request)

    product_list = cart.get_email_values()
    context = {
        'product_list': product_list
    }
    message = render_to_string('cart/order_email.html', context)
    subject, from_email, to_emails = "New order", settings.EMAIL_HOST_USER, ["EMAIL TO SEND"]
    email = EmailMessage(subject, message, to=to_emails, from_email=from_email)
    email.content_subtype = 'html'
    email.send()
    cart.clear()
    return redirect('cart:CartDetail')
