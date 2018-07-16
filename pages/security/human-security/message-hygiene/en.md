@title = "Message Hygiene"
@toc = true
@summary = "Simple tips for using email and messaging more safely"

# Never trust the sender

The primary reason that email is the source of most attacks in an organization is that there is no way to verify the identity of the "From" address.

Let's repeat that: Anyone can spoof the "From" address and can make any email appear to come from anyone else.

Because it is difficult to verify the sender, your inbox is a common source of **Phishing Attacks** and **Malware Attacks**.

* **Phishing Attack** is when someone sends an email claiming to be an entity they are not, and uses this deception to get information. They can be after social security numbers, bank information, passwords, or other sensitive information.
* **Malware Attack** is when an attacker attempts to trick you into installing malicious software on your computer when you open an attachment or click on a link.

Generally, anything unexpected in your email should be looked at with suspicion. Be wary of any messages that ask you to do something, including clicking a link, opening an attachment, or emailing back information - even if they are from someone you know!

If someone has broken into your account, you may see reply messages you don't understand, additional sent items, new folders or filters being created, or other changes to settings. Suspicious emails or account behavior should be reported to a technical support person and you should preemptively change your password.

# Avoid links in emails

Links, often innocuous looking or even hidden within emails, are the major way attackers steal your data and take over your devices.

The best practice is to never click links in emails. If you must click a link, follow this checklist:

* Are you expecting this email? Even if the "From" address appears to belong to someone you know, you should be very cautious when you receive an unexpected email.
* Can you manually type the link instead of clicking on it? What you see in the link might not be what the link really is. Domain names can contain "homographs", or different characters that look the same (e.g. the number "0" and an uppercase "O", or between Latin and Cyrillic charsets). That link that appears to be <https://riseup.net> might actually point to an attacker's website at <%= '<a href="https://riseuρ.net">https://riseuρ.net</a>' %> (the second link uses a Greek letter for the "p"). The safest way for users avoid this attack is to never copy URLs from unsafe sources and always type URLs to the address bar directly.
* Do you recognize the domain? In most email programs, as on the web, hovering over a link displays the URL it points to. If the link's destination is unexpected or unfamiliar, check with the sender to make sure the email is legitimate. The link should always start with "https://". If it starts with "data://", then it is certainly a phishing attack.

Never click on links or open files from unknown senders or in otherwise suspicious emails. Unlike people you know and are working with, someone you don't know will never send you a file that you actually need; if a link from an unknown sender actually contains useful information, you will be able to access it via another, more trusted method (for example, a web search).

# Never log in after clicking a link

If you do click a link in your email, it is very important to not log in to the website that is opened. If the website prompts you to log in, you should instead follow these steps:

1. Open a new tab in the browser, and type the domain of the website manually.
2. Using this new tab, log in to the website.
3. Go back to your email and click on the link again.
4. When this link opens, it should not require you to log in. If it does require that you log in, then the email is probably a phishing attack.

This practice will protect you from most phishing attacks.

# Avoid attachments

Email attachments present several risks, including their use as a mechanism for phishing. They are not protected from being viewed or altered between recipients, so you cannot ensure that the document you send is the same one that the recipient receives. A malicious server between you and the sender could replace it with any program or file they want, including a virus or malware. Additionally, file attachments tend to remain in recipients' email in-boxes, where they are harder to control. For example, if you filled out an order form using your organizational credit card, and emailed it to a vendor as a PDF, someone who breached their email account would have access to a document containing your credit card information for as long as it was not deleted from the server.

A better practice than email attachments is to have files on a server and send links to documents instead of the documents themselves. Ideally these links lead to locations that themselves are protected by passwords or other authentication, or are temporary and expire soon after use. These links can be easily generated in almost all file-storage systems, whether they use servers in your office (such as a Windows file server) or on the web (such as Google Drive, Box, or Dropbox).

For added security, you can share encrypted files via temporary links by uploading files to <https://share.riseup.net>.

# See also

* [Security Self-defense / How to Avoid Phishing Attacks](https://ssd.eff.org/en/module/how-avoid-phishing-attacks)
* [Security Education Companion / Phishing and Malware](https://sec.eff.org/topics/phishing-and-malware)
* [Security In-a-box / Protect Your Device From Malware and Hackers](https://securityinabox.org/en/guide/malware/)
* [Security In-a-box / Keep Your Online Communications Private](https://securityinabox.org/en/guide/secure-communication/)
* [Security Planner / Spot Suspicious Emails](https://securityplanner.org/#/tool/spot-suspicious-emails)
