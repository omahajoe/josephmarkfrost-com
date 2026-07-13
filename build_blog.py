#!/usr/bin/env python3
"""One-time generator for blog pages. Content migrated verbatim from WordPress 2026-07-13."""
import os, html

OUT = os.path.dirname(os.path.abspath(__file__))
BIO_4X = """<p class="bio">Joseph Frost is a Decentralized Entrepreneur, University Professor of Entrepreneurship &amp; 5X Founder. He is the Founder of <a href="https://guidedoutsourcing.com/">Guided Outsourcing</a>, a people-centric outsourcing business, and <a href="https://yorcmo.com/">yorCMO</a>, the first Decentralized Leadership marketing system. He is also the host of the weekly podcast “The Fractional C-Suite Retreat.” — <a href="https://www.linkedin.com/in/josephfrost/">LinkedIn</a> · <a href="mailto:joe@josephmarkfrost.com">Email</a></p>"""

SHELL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — Joseph Mark Frost</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../styles.css">
</head>
<body>
<header class="site">
  <div class="wrap">
    <a class="logo" href="../">JOE<span>FROST</span></a>
    <nav class="main">
      <a href="../">Home</a>
      <a href="./">Blog</a>
      <a href="../#talks">Keynote Speaking</a>
      <a href="../#testimonials">Testimonials</a>
    </nav>
    <a class="btn" href="../#contact-joe">Book Joe to Speak</a>
  </div>
</header>
{body}
<footer class="site">
  <div class="wrap">
    <div class="copyright">© 2026 Joseph Mark Frost · All Rights Reserved · <a href="../">Home</a> · <a href="./">Blog</a></div>
  </div>
</footer>
</body>
</html>"""

def post_page(title, date, cats, body_html, desc):
    body = f"""<section class="post-hero">
  <div class="wrap">
    <h1>{title}</h1>
    <div class="meta">By Joseph Frost · {date} · {cats}</div>
  </div>
</section>
<article class="post-body">
{body_html}
</article>"""
    return SHELL.format(title=html.escape(title), desc=html.escape(desc), body=body)

POSTS = [
 dict(slug="cup-of-joe-monetizing-scope-creep",
  title="Cup of Joe Recap: Stop Fearing Scope Creep — Say “Yes, And”",
  date="July 13, 2026", cats="Cup of Joe, Fractional Practice",
  desc="From this week's Cup of Joe LinkedIn Live: how fractionals turn scope creep from a threat into a monetization opportunity — plus the 7 A-referral-partner math.",
  img="https://josephmarkfrost.com/wp-content/uploads/2021/02/JoeFrost.jpeg",
  excerpt="This week on Cup of Joe, Robert and I finished the lead-sources conversation and dug into the second distraction: worrying about scope creep instead of monetizing it...",
  body="""<p><em>Every week, my co-host Robert Mendelson and I go live on LinkedIn for <strong>Cup of Joe</strong> — real questions from real fractionals, no scripts. This week's session is brought to you by <a href="https://yorcmo.ai">yorCMO.ai</a>. Here's what we covered.</em></p>
<h3>First, the leftover question: what do you do with a bad referral from Uncle Bob?</h3>
<p>You told the family you're looking for referrals. Uncle Bob connects you with Charlie. Thirty seconds into the call you know it's a bad fit. Now what?</p>
<p>Handle it like any other bad referral: run your process, point Charlie in a better direction, and don't overthink it. The only question that matters is whether Bob is ever going to be an A or B referral partner. If he is, go back and educate him — “thanks for that referral; here's what my ideal client actually looks like.” If he isn't, don't bother. Friends and family are rarely your A-partners; they're the wide net that bumps into an opportunity for you once in a while. Stay diplomatic and appreciate the give, even when it's a rotten one.</p>
<h3>The math: seven A-partners runs your whole pipeline</h3>
<p>Over the last eight years at yorCMO we've closed about <strong>one out of every seven qualified opportunities</strong>. So if you want four new clients a year, you need 28 qualified opportunities. Where do 28 qualified referrals come from? <strong>Seven A-referral partners, each sending you one qualified lead per quarter.</strong></p>
<p>An A-partner is someone who's in front of your target audience regularly, has ongoing opportunities to refer you, and actually sends one qualified referral a quarter. It's not a big ask — but you may have to go through a couple hundred coffees to find your seven. That's the game. Seven relationships handle your entire business development; the rest is scaling delivery.</p>
<h3>The second distraction: worrying about scope creep instead of monetizing it</h3>
<p>Every fractional knows the feeling — the slow expansion of tasks that leaves you overworked and undervalued. The standard advice is “just say no and defend the scope.” I think that's the distraction.</p>
<p>Every scope-creep request is a <strong>real need</strong>. The client wouldn't ask otherwise. So the answer isn't “no, but” — it's <strong>“yes, and”</strong>:</p>
<ul>
<li><strong>Yes, and</strong> I can bring in another fractional from my network to handle it.</li>
<li><strong>Yes, and</strong> we can add budget this quarter to make room for it.</li>
<li><strong>Yes, and</strong> I have a vendor partner who's excellent at this — let me get you a proposal.</li>
<li><strong>Yes, and</strong> what should we remove from this quarter's sprint to prioritize it?</li>
</ul>
<p>Each of those paths monetizes the request — new budget, a referral fee, or the reciprocal value of putting an opportunity in a partner's lap.</p>
<h3>The vendor trap</h3>
<p>Here's the line I want every fractional to remember: <strong>as soon as you start doing vendor work, you become a vendor again — not a strategic partner.</strong></p>
<p>Even when the ask is a 15-minute task you could knock out yourself, the answer is “yes, I'll get it done” — through your coordinator, your bench, or your vendor partner. A strategic leader doesn't say “I don't do that” (off-putting, and untrue). A strategic leader says “I'll get it done.” Do it once as a favor and route it visibly through your network; if it keeps coming up, that's a budget conversation the client is now primed to say yes to.</p>
<h3>On referral fees: fiduciary means transparent, not broke</h3>
<p>Some fractionals refuse referral fees outright on fiduciary grounds. That's legitimate. But being a fiduciary can also mean taking the fee <em>and being transparent about it</em>: it doesn't change the client's price, and you disclose that some vendor partners have a referral relationship with you. In my experience, clients who trust you don't care — as long as the vendor is good and the price is honest. Find partners who don't jack up the price to fund the fee, and disclosure stops being awkward.</p>
<h3>Put it in the agreement</h3>
<p>Every yorCMO agreement says it up front: out-of-scope requests will happen every quarter, and here's how we handle them — defer, swap, or add budget. Companies that focus on fewer things get better outcomes; that's the whole rocks-and-pebbles conversation. Set it at the onset and the quarterly scope conversation becomes comfortable instead of confrontational.</p>
<p><em>Next week on Cup of Joe: Distraction #3 — selling industry-agnostic vs. specializing. Or as Robert put it: how to get over “I'm good at everything” syndrome. <a href="https://www.linkedin.com/in/josephfrost/">Follow me on LinkedIn</a> to catch it live, and if you want the full system behind the five distractions, that's the <a href="https://frost-framework.com">FROST Framework</a>.</em></p>"""),

 dict(slug="chasing-leads-vs-building-lead-sources",
  title="The First Distraction: Chasing Leads vs. Building Lead Sources",
  date="July 13, 2026", cats="FROST Framework, Fractional Practice",
  desc="Most fractional consultants spend 80% of their energy chasing individual leads when they should be building lead sources. Part 1 of the Five Distractions series.",
  img="assets/frost-infographic-1.png",
  excerpt="Most fractionals spend 80% of their energy chasing individual leads when they should be building lead sources — repeatable systems that send clients to you...",
  body="""<p><em>This is Part 1 of the <strong>Five Distractions</strong> series — the five places fractional consultants pour energy that quietly keep them from building a real firm. It's drawn from the <a href="https://frost-framework.com">FROST Framework</a>, the system I teach for building a million-dollar fractional practice.</em></p>
<h3>The problem with chasing leads</h3>
<p>Most fractional consultants spend 80% of their energy chasing individual leads when they should be building <strong>lead sources</strong>.</p>
<p>The difference sounds subtle. It isn't. A lead is one opportunity — you win it or lose it, and either way you start over at zero tomorrow. A lead source is a <strong>repeatable system that sends clients to you</strong> without constant outbound effort. Chasing leads is a treadmill. Building lead sources is an asset.</p>
<h3>The three types of lead sources</h3>
<p><strong>1. Other fractionals (the best).</strong> Your peers get asked for things outside their scope constantly — and they refer those opportunities to someone. A network of fractionals who know exactly what you do and trust you with their clients is a business-changing asset.</p>
<p><strong>2. Business groups (good).</strong> Strategic partnerships with complementary service providers, SaaS tools, and agencies who serve your audience and see your kind of opportunity before you do.</p>
<p><strong>3. Your personal network (the baseline).</strong> People who already trust you and refer when they can. Valuable — but rarely your engine, because they only occasionally bump into your ideal client.</p>
<h3>The 7 A-referral-partners formula</h3>
<p>Here's the math I use with our own CMOs, built on eight years of pipeline data:</p>
<ul>
<li>One A-partner sends you <strong>one qualified lead per quarter</strong> — 4 per year</li>
<li><strong>7 partners × 1 referral/quarter = 28 qualified leads per year</strong></li>
<li>At a 1-in-7 close rate, that's <strong>4 closed deals a year</strong></li>
</ul>
<p>For most fractional practices, four good engagements a year <em>is</em> the business. Which means seven solid relationships handle your entire business development — and everything else is scaling delivery. You may need a couple hundred coffees to find your seven. Worth every cup.</p>
<h3>Do this now</h3>
<ul>
<li><strong>Map your current lead sources.</strong> Where did your last 10 clients actually come from? Which ones took the most work?</li>
<li><strong>Find your gaps.</strong> Are you living on outbound? Do you have a single true referral partnership?</li>
<li><strong>Target your first 3 A-partners.</strong> Who would refer you most naturally? Start those conversations this week.</li>
</ul>
<p><em>The full lesson — including the Lead Source Mapper tool that does the mapping with you — is inside the <a href="https://frost-framework.com">FROST Framework course</a>. Next in the series: <a href="cup-of-joe-monetizing-scope-creep.html">Distraction #2 — worrying about scope creep instead of monetizing it</a>.</em></p>"""),

 dict(slug="why-i-started-the-largest-community-of-fractional-professionals",
  title="Why I Started the Largest Community of Fractional Professionals (and Why You Should Join)",
  date="April 9, 2023", cats="Business, Collective, Strategy",
  desc="Why Joseph Frost built the Fractional Professionals Association — and why fractional professionals should join.",
  img="https://josephmarkfrost.com/wp-content/uploads/2023/03/Joe-Frost-Posts.png",
  excerpt="As the co-founder of a rapidly-scaling fractional CMO business (yorCMO) and as a big fan of fractional...",
  body="""<p>As the co-founder of a rapidly-scaling fractional CMO business (<a href="https://yorcmo.com/">yorCMO</a>) and as a big fan of fractional professionals in general, I looked far and wide for a centralized hub where the world’s best fractional professionals could be found. My search resulted in one clear conclusion: there wasn’t a true community for fractional folks. No hub for sharing resources, no place for interaction and learning, and no way to collaborate and partner on prospective projects. Most fractional professionals never interacted with each other at all.</p>
<p>Well, that’s no good, is it? Surely, something can be done about it, I thought.</p>
<p>So, I did! I formed the <a href="https://fractionalpros.com/">Fractional Professionals Association (FPA)</a> with the help of <a href="https://www.linkedin.com/in/richardtaylor/">Rich Taylor</a>. At FPA, we promote and support decentralized leadership, ideate and innovate, facilitate growth, and make life better for ourselves and our clients.</p>
<p>There are three main reasons why I built the largest community of fractional professionals in the world – reasons which also make it well worth joining if you are a fractional professional yourself.</p>
<h3>A Need for Improved Visibility, Collaboration, and New Opportunities</h3>
<p>ADP previously reported that, from 2010 to 2019, the number of contractors working for companies had increased by 15%. The pandemic amplified this change, with nearly one in five (17%) knowledge workers considering joining the gig economy in 2022 according to Paro via Forbes. As the U.S. saw its largest number of resignations since it started recording data, the number of applications submitted to launch new businesses increased by 1 million compared to the same time period the year before. Many of those “resigners” were executives who went to start their own consulting or fractional practice.</p>
<p>Unlike freelancers, fractional professionals don’t work “alone”: they are active members of an organization for a fraction of the time. Still, the reality of a fractional professional is a unique one.</p>
<p>As our fractional CMO business <a href="https://yorcmo.com/">yorCMO</a> began to grow, we learned that fractional marketing leaders shared a desire to collaborate and increase their visibility. Existing communities didn’t solve their need for connection as these focused on either full-time professionals or freelance or consultants, so we engineered our own. Eventually, we realized it wasn’t just CMOs who wanted to connect with each other; the need for community was felt across fractional C-level leaders from finance to sales to operations and tech and beyond. The FPA was born – and continues to thrive – on its commitment to building true community for its members.</p>
<p>There is so much value in connecting with like-minded people, both for fractional professionals and for their clients. Members now have an environment where they can share leads and opportunities, expand their network, collaborate and ideate, and generate plenty of buzz about their fractional biz.</p>
<p>It’s also how fractional professionals stay ahead of industry trends – and sometimes pioneer a few of them ourselves. The more ideas the community can generate together, the more companies for which fractional professionals work get to benefit. In the process, real connections and collaborations can be had, which I cannot help but feel inspired by.</p>
<h3>Access to Knowledge, Resources, and Events</h3>
<p>I’ve been a member of numerous peer groups over the years primarily in the entrepreneurial space. The best peer groups function like a community in a small town where every “neighbor” lends invaluable insights rather than a cup of sugar. And the results are all the sweeter for it. Along the way, we’ve learned that our stories can help each other grow and thrive as individuals with something special to offer prospective clients.</p>
<p>This ability to learn from one another’s insights has paved the way for new growth opportunities and resources (including VA sourcing, personal branding services, and multi-channel lead generation <a href="https://fractionalpros.com/resources/">as detailed on our website</a>). When a community shares knowledge, solutions and resources grow rapidly. Everyone’s fractional business benefits.</p>
<p>There are also special events, like our first-ever in-person Fractional Professionals Association Conference event taking place in late 2023 (I am beyond hyped for this one). There is no in-person event quite like it. Beyond the community and connectedness, it’s the learning portion I am most excited about. The event is slated to feature a ton of remarkable speakers, thinkers, and ideators on best practices, trends, and opportunities for fractional professionals to capitalize on to scale their practice.</p>
<p>Whether it’s our monthly speaker series or an in-person super-conference, FPA continues to act as a bridge linking community members to resources and knowledge. Whether one has been a fractional professional for years or is considering taking the leap into the fractional world for the first time, there’s something for everyone to learn.</p>
<h3>Fostering Connections – and Growth</h3>
<p>Naturally, all these efforts enable members to form connections with each other – and can act as an additional source of leads for one’s fractional business. The more fractional professionals connect with each other, the more they can exchange opportunities, bring each other onto fractional mandates, or make introductions to companies in their network. Companies suddenly go from where I originally found myself (“Where are all these fractional professionals, anyway?”) to having second-degree access to an entire network of fractional professionals in diverse verticals. Prospects can harness new talent in a way that is more affordable and more committed than consultants or freelancers, and fractional talent can work together to help companies reach their goals.</p>
<p>Our dedicated matrix is as cool as what it sounds like, syncing prospects to members and bridging the gap without overlooking any specific requirements on either end. Having the largest association of fractional professionals around is the secret sauce that makes it work so well! Building a rapport with like-minded fractional professionals can be not only rewarding workwise, but also a whole lot of fun.</p>
<p>By fostering growth, we’re able to continually motivate and push each other to achieve success with our individual practices, and having a decentralized environment where we can interact with each other is a big part of that.</p>
<h3>Conclusion (and an Invitation)</h3>
<p>It’s an exciting time to be in the fractional space. Our community is continuing to grow. With continued development, innovation, and collaboration, we’re celebrating new wins daily – often in tandem with our clients.</p>
<p>A huge thanks to Rich and the rest of the team who made this wonderful, inclusive, and passionate community possible. Our incredible leadership group deserves a round of applause, consisting of early adopters who have lent their infectious energy and insights. Among them is Klarissa, based in the Philippines, who keeps the gears oiled and churning efficiently behind the scenes – super grateful to have you with us! It’s been an honor to be a part of the journey, and the future looks bright, much like the individual spotlights shining down on our members.</p>
<p>Whether you’re a partner, practitioner, or prospect, we’d love to connect. Consider this my personal invitation to you. If you’re seeking the finest talent that aligns with your organization’s needs, you’ve come to the right place.</p>
<p>Alternatively, if you’re a fractional professional looking for <a href="https://fractionalpros.com/">a proper community</a>, then welcome home – you’ve found it!</p>"""),

 dict(slug="4-ways-to-leverage-podcasting-to-grow-your-business",
  title="4 Ways to Leverage Podcasting to Grow Your Business",
  date="September 29, 2022", cats="Business, Podcast, Strategy",
  desc="Why every entrepreneur, leader or fractional professional should consider incorporating a podcast into their business model.",
  img="https://josephmarkfrost.com/wp-content/uploads/2022/09/Copy-of-Joe-Frost-1.png",
  excerpt="When I first launched my podcast, The Fractional C-Suite Retreat, I had no idea what would come from...",
  body="""<p>When I first launched my podcast, <a href="https://www.fractionalcsuiteretreat.com/">The Fractional C-Suite Retreat</a>, I had no idea what would come from it. The actual process of making a podcast is surprisingly straightforward. The three key ingredients: a computer to record the podcast, a good microphone to capture your voice, and a software program to edit your audio. (Some say a fourth requirement is an attractive voice…but if I made it, so can you.)</p>
<p>The hardest part of podcasting? It’s nothing related to sound engineering or fancy marketing strategies. It’s the ability to find that bedrock idea that ties it all together.</p>
<p>A unique angle is critical – and with the rapid growth of podcasts as a media form built for communities, going niche and specific is key. However, the most important element I’ve learned throughout my podcasting experience: identifying a purpose for the podcast you want to launch.</p>
<p>Podcasting is an exercise in longevity. Identifying a big mission or purpose – the reason why you started this thing in the first place – will propel you forward on the days you feel too busy or too low on energy. Most likely your purpose lies in the audience you strive to inspire or the feeling you get when you are deep in discussion with a guest. Financial gains will come, but lead generation and monetary ROI cannot be the primary motivator (money alone is never a sustainable driver for anything, I’ve learned).</p>
<p>The results and impact a podcast creates far outweigh the challenges. The benefits are so significant that I believe every entrepreneur, leader or fractional professional should consider incorporating a podcast into their business model. The reasons are straightforward.</p>
<h3>Branding &amp; Marketing</h3>
<p>When I first started my podcast, I knew I wanted it to support the latest business I was building (<a href="https://yorcmo.com/">yorCMO</a>: a fractional CMO company). I was quickly getting fascinated with the fractional model of work – and I wanted a platform to share my excitement for it while speaking directly to the audience my business was targeting.</p>
<p>A podcast is a marketing channel – and it can be a key part of a strategic marketing mix. But there was one small difference: the podcast wasn’t a Facebook ad being spread across the internet by a faceless corporate brand. The podcast was me: my voice, my thoughts, the types of guests I felt excited about speaking to. It was my brand.</p>
<p>The concept is simple: a show meant for an executive audience to listen to while unwinding and learning about various issues affecting the C-suite. I had always loved (still do) reading, listening to a podcast or writing over a cigar in my backyard after a long day. I figured other busy leaders might already be doing the same thing I did, and they might want to join in my cigar-fueled audio retreat.</p>
<p>While branding the podcast, I was able to brand my company and myself at the same time to my listeners. Talking about shared experiences with my guests makes listeners associate certain feelings with me and, by extension, the company I founded. The podcast began to act as a supporting pillar of my corporate brand’s marketing and my own personal brand’s marketing.</p>
<p>What’s more: a steady flow of episodes started to fuel content for social media accounts.</p>
<p>From a branding perspective, a podcast can be invaluable: it can create some valuable online engagement for your brand(s) while giving you marketing content for your other channels.</p>
<h3>Audience Connection and Authoritative Presence</h3>
<p>The name of the podcasting game? Creating personal connection in today’s disconnected world.</p>
<p>Podcasting establishes a more direct connection to your audience. While blogs and posts on social media are used to connect with your audience, podcasting has a unique place in the social media landscape. Your audience hears your voice and mannerisms in ways that texts cannot compete with.</p>
<p>Do podcasts for a long enough time, and you will have an audience who simply loves listening to your (and your guests’) thoughts. If your voice is an authentic one, and if you hold back from the temptation to make everything “perfect,” your audience will see you as an authoritative figure on your core topic; they’ll get to know you, and feel you understand them; and inadvertently they’ll develop a sense of trust.</p>
<p>The goal isn’t to be a “thought leader”; it’s to be an unfiltered, interesting, reliable lighthouse standing out in a crowded sea of voices guiding your audience home. Be the lighthouse!</p>
<h3>New Avenues for Online Presence</h3>
<p>Whether for your corporate brand or for your personal brand (or both, if they are interconnected), a podcast is a smart way to reach audiences outside of your immediate industry or network.</p>
<p>Podcasting helps your business reach an audience disconnected from but adjacent to all your other marketing channels. Traditional marketing rhetoric tells us to be on “every” social media platform – but more often than not we end up focusing on one platform above the rest (which is likely a smarter strategy). Most commonly, it’s the one where the biggest concentration of our target audience is found.</p>
<p>Podcasting is, in some ways, natively disconnected from a singular social media platform – which means it creates opportunities to reach people you have never met, known about, or marketed to.</p>
<p>According to the Infinite Dial 2021 survey by Edison Research on digital media consumer behavior in the United States, 41% of the US population listens to podcasts monthly. In 2012, this percentage was only 14%.</p>
<p>It’s a rapidly-growing segment – one that is diversifying in terms of appeal. The same survey notes that podcast listeners’ demographics (gender, ethnicity, and age) are diversifying just as rapidly. The interest in podcasts is not only an American phenomenon: Latin America and Asia Pacific, for example, have seen remarkable growth.</p>
<p>The point: podcasting creates new avenues for new exposure to new audiences – and despite what seems like a “crowded” podcasting market, in some ways it’s still in its infancy as a channel to reach and inspire audiences.</p>
<h3>Building a Learned Community</h3>
<p>Nothing beats honest intellectual conversations.</p>
<p>A main (and understated) benefit of podcasting: getting to have conversations with smart, interesting people. I’ve had many wonderful guests of various backgrounds on my podcast, from whom I learned so much about different facets of business. One week I am talking to a world-class expert about modern-day marketing; another week on company culture; the next about the future of work.</p>
<p>Beyond the concepts related to your core topic (in my case, executive business leadership issues), I’ve learned so much about psychology, philosophy, health, strategic thinking, relationship-building, and much more. The guests I’ve had on my podcast continuously remind me and my audience that no matter how experienced you may be in your field of expertise, there are always new things to learn.</p>
<p>Moreover, the simple act of having guests on a weekly podcast builds a sense of community: I’ve expanded my network and audiences exponentially; built real relationships I will hold onto; and have received messages on how I’ve inspired others to achieve their goals. Even if a podcast is by default a one-way conversation, a community gets created where people can exchange, learn and grow. It’s remarkable, really.</p>
<p>Whether you are a seasoned entrepreneur or a C-level leader who made the recent leap to go fractional, I believe podcasting can help your business grow.</p>
<p>My suggestion: give it a try. Start with a mission and purpose – and who knows where the podcasting journey can take you from there?</p>"""),

 dict(slug="winter-is-coming-documentary",
  title="Winter is Coming: A Documentary Film about Surviving the Seasons of Entrepreneurship",
  date="May 9, 2022", cats="Business",
  desc="Winter is Coming: A Documentary Film about Surviving the Seasons of Entrepreneurship produced by Joe Frost.",
  img="https://josephmarkfrost.com/wp-content/uploads/2022/05/Welcome-1024x1024.png",
  excerpt="One of the highlights of my professional life has been making “Winter is Coming,” a documentary...",
  body="""<p>One of the highlights of my professional life has been making “Winter is Coming,” a documentary film on the four seasons of entrepreneurship.</p>
<p>If you are an entrepreneur, current or past, you will relate: the cyclical, almost inevitable crises we all face throughout the day-to-day rollercoaster of building a business. Survival is not guaranteed – but learning, growth and transformation always is.</p>
<p>The film discusses the crises or “winters” in different cycles of business. Four entrepreneurs (myself included) share their experiences surviving four different types of crises. They all share one bond: a thirst for learning.</p>
<p>This is an ideal film for any business, nonprofit, or organization interested in exploring the Seasons of Entrepreneurship further. If you want to schedule a private screening or just learn more about the film please <a href="../#contact-joe">get in touch</a>.</p>
<p>Know an entrepreneur who might be struggling through a “winter” right now? Share this with them – here is hoping it might help them.</p>
<p>Watch the documentary below and visit the <a href="https://www.seasonsofentrepreneurship.com/">full website here</a>. Enjoy the viewing.</p>
<p>Joe</p>
<div class="video-frame" style="margin-top:28px"><iframe src="https://fast.wistia.net/embed/iframe/efqd4qwmxq" allowfullscreen style="width:100%;aspect-ratio:16/9;border:0"></iframe></div>"""),

 dict(slug="why-the-future-of-work-is-fractional",
  title="Decentralized Leadership: Why the Future of Work is Fractional",
  date="April 10, 2022", cats="Business, Strategy",
  desc="The new model of hiring: decentralized leadership. When a leader works part-time, spending less time and money than a full-time leader.",
  img="https://josephmarkfrost.com/wp-content/uploads/2022/04/Joe-Frost.png",
  excerpt="The world is changing faster than it ever has. Out of those changes emerges a new model of decentralized leadership: fractional...",
  body="""<p>The world is changing faster than it ever has. Out of those changes emerges a new model of decentralized leadership: fractional.</p>
<p>“Fractional” leadership inherently implies a definition that is easily understood: an executive leader joins an organization on a flexible, part-time, basis, spending a fraction of the time of a full-time leader and comes at a fraction of the cost.</p>
<p>However, the term “fractional” also implies smallness, fragmentation, incompletion. Leaders joining an organization in a fractional capacity are anything but small or fragmented – and neither is the impact they bring to a growing company. We knew there was a better way of defining the model.</p>
<p>To re-evaluate the leadership and hiring model of the future, we started by understanding what leadership of the future looked like. Modern leadership would:</p>
<ul>
<li>Relinquish centralized control of knowledge</li>
<li>Always lead with empathy &amp; transparency rather than authority</li>
<li>Encourage flexibility</li>
<li>Understand, embrace &amp; prepare for the future of work</li>
<li>Leverage external expertise &amp; believe in the power of community</li>
</ul>
<p>The model for modern leadership looked familiar. We saw an opportunity to re-evaluate the fractional concept through a deeper lens. The “fractional” business model is, in reality, <em>decentralized</em>.</p>
<h3>Inspired by Blockchain</h3>
<p>You don’t need to be a Blockchain expert to know that decentralization as a concept has gained traction rapidly. While Blockchain may have popularized the concept, a new definition for decentralization is developing in the context of the future of work – one which had not been applied previously. From our view, decentralization is not only tangential to but entirely <em>essential</em> to the future of work.</p>
<p>Re-evaluating the fractional concept by means of decentralization brings the model closer to a more authentic reality – one which reflected (almost eerily-so) the future of modern leadership.</p>
<p>At its core, Blockchain:</p>
<ul>
<li>Eliminates aggregated central control</li>
<li>Is rooted in outsourcing</li>
<li>Facilitates P2P (peer-to-peer) engagement</li>
<li>Is dependant on network dynamics</li>
<li>Bolsters flexibility &amp; independence</li>
<li>Creates a paradigm shift in business models &amp; revenue creation</li>
</ul>
<p>Ultimately, we realized the fractional model is a decentralized one. Like Blockchain principles, a decentralized hiring model seeks to transfer power and authority to lower levels of an organization, flattening hierarchies and creating a deeper sense of equality and interdependence, rather than authority, between leaders and teams. In a decentralized model, knowledge ripples across an organization, silos are eliminated and leaders are connected to teams in a real way.</p>
<p>But before diving into the ways in which decentralized leadership can ignite an organization’s future, let’s take a brief look to the past.</p>
<h3>A Brief History of Decentralization</h3>
<p>Historically, “decentralization” has been used as a political term signifying a reduction in the authority of national governments over policymaking. The Center for International Earth Science Information Network (CIESIN) of Columbia University, for example, defines decentralization as “the transfer of part of the powers of the central government to regional or local authorities.” CIESIN argues that decentralization in governance is a by-product of local governments and civil society wanting to be more involved in the managing their own local affairs.</p>
<p>In more recent years, decentralization has come to be attached to decision-making. Peoplehum, a HR technology platform, defines decentralization as the “specific form of organizational structure where the top management delegates decision-making responsibilities and daily operations to middle and lower subordinates.” By transferring decision-making responsibilities, the C-Suite is left with more time, energy and focus to grappling with strategic decision-making which affects the organization as a whole. While decentralized leadership does impact decision-making structures within an organization, its impact goes far beyond decision architecture.</p>
<p>Once decentralization became embraced by Blockchain, its definition took on an altogether expanded meaning – one that would bring it squarely into the future.</p>
<p>MIT’s Journal of Design and Science (JoDS) suggests that, because “blockchains are not controlled by a central authority, but by the entire network of participants, who establish the rules for participation themselves and can elect to evolve the system according to consensus,” Blockchain offers an alternative to Silicon Valley’s monopolized technological development. Again and again, decentralization as a concept is defined as the transferring of centralized powers into more local or subordinate actors in the context of hierarchies. It is an egalitarian and democratic philosophy – but how does it apply to leadership, to small businesses, to entrepreneurs and to the future of the workplace?</p>
<h3>Future of Work</h3>
<p>The future of work is here – and it looks entirely different than average businesses, small or large, have been used to.</p>
<p>A record 4.3 million Americans quit their jobs in one month in 2021 (December). Recent research shows that more than 40% of the global workforce are considering leaving their employers this year. As resignations rise, alternative models for working are gaining traction – rapidly.</p>
<p>Over the next five years, 52% of the U.S. adult workforce will either be working or will have worked as an independent contributor. 63% of full-time executives confirmed they would become an independent contractor, given the opportunity. The consulting, independent &amp; fractional economy is one of the fastest-growing phenomena in the country.</p>
<p>According to an Intuit 2020 report, 80% of US companies plan to use a flexible, non-traditional workforce. Likewise, Harvard Business Review has reported that approximately 150 million people in the US and Western Europe currently work as independent contractors.</p>
<p>In a post-pandemic world of work, the “Great Resignation” continues to transform the way companies operate. As technology continues to usher in new ways to run our companies, one thing has become clear: the leadership model of the future is decentralized.</p>
<p>However, the “Great Resignation” can also become our greatest opportunity.</p>
<p>After a mass exodus of leaders and teams from traditional employment structures, a new period in economic history is set to begin: the “Great Rehire” – though it will look radically different from what traditional hiring has looked like. A decentralized leadership model values flexibility, relinquishes centralized control structures, and brings more objectivity, freshness of perspective, and creative ideation – and it is set to transform the post-pandemic workplace.</p>
<h3>Benefits of Decentralization</h3>
<p>Decentralized hiring models for leadership hold numerous benefits – and the organizations already employing the model are seeing major returns across productivity, culture and governance pillars within their organizations.</p>
<h3>Diversity of Thought</h3>
<p>Decentralized hiring, the strategic implementation of fractional and part-time leaders within the C-Suite, is non geo-centric: in a remote-first world of work, organizations have access to a broader and more diverse talent pool to scale their teams.</p>
<p>With traditional geographic boundaries eliminated from the equation, organizations have more options to bring specific, niche expertise from across their industry or outside of their industry. Expertise within the organization can reach new heights, and diversity is driven up, both in terms of cultural background and in terms of thought. Hidden biases stemming from an entirely-local talent pool which often make their way into traditional hiring practices, like conformity bias (also called “Groupthink”), are quickly eradicated.</p>
<h3>A Culture of Decision-Making</h3>
<p>Decentralized leaders are often only physically (or virtually) present a fraction of the average work week. As a result, a culture of decentralization becomes a culture of decision-making: mid-level teams become empowered to own their own decision-making capabilities without the necessity of turning to a direct ever-present leader for continuous streams of approvals. As a result, with time, teams become more autonomous and more productive. Likely, teams that own their own decision-making will also see an increase sense of happiness and satisfaction in their role. It’s been said that “meaning is the new money”: if 9 out of 10 people are willing to earn less money to do more meaningful work, the companies of tomorrow are incentivized to ensure meaning, autonomy, and satisfaction are core to daily operational culture.</p>
<p>As a result of a shift in decision-making hierarchies, the C-Suite becomes liberated, with a lesser cognitive load and more time to focus on strategic planning (which, arguably, increases their own satisfaction with their role). Micro-management is systematized out, by design; strategic and critical thinking is systematized in.</p>
<h3>Embracing Equity</h3>
<p>Decentralization fosters a more equitable culture by flattening an organization’s structure. Fractional executives who, coming in as part-time or independent leaders, often bring a genuine, deep enthusiasm to a company’s success – one that is entirely different from the traditional employer-employee work dynamic. Suddenly, an external leader coming internally to an organization develops a deep commitment to the company’s mission, vision, values and big goals.</p>
<p>The paradigm shift from “You work for me” to “I work for me and you,” interlinking each person’s success, creates an environment where all employees and leaders share common objectives and aligned incentives. Teams feel more supported instead of less – and a strong sense of belonging is created. Power dynamics shift when aggregated control centers, as with Blockchain, are eliminated.</p>
<p>Ultimately, decentralized work environments are empowered ones where employees can make their own decisions in local matters, empowering them to take higher ownership over their role. Ownership and leadership teams benefit from heightened efficiency, speedier decision-making, increased adaptability, and a more egalitarian and diverse work culture. Organizations become more creative, save more costs, are infused with more energy, have access to talent and ideas they would not normally have access to, and become more flexible in a way that traditional corporate structures simply cannot be.</p>
<p>The fractional leadership model is a decentralized one – and it can be adapted seamlessly for smaller, founder-run organizations or larger, C-Suite-run organizations equally.</p>
<h3>Implementing Decentralized Leadership</h3>
<p>The benefits of the decentralized, fractional model are clear – and the next step is implementation. Key questions remain, including:</p>
<ul>
<li>How can entrepreneurs implement the power of fractional professionals to prepare for the future of work?</li>
<li>How can we leverage it to create kinetic energy that attracts high-calibre prospective clients and employees?</li>
<li>How can a fractional, decentralized model for hiring leaders help our organizations combust at scale?</li>
</ul>
<p>Nobody knows with certainty what the business world of tomorrow will look like. Yet, one thing is clear: as the world continues to evolve and transform rapidly, it is our role as entrepreneurs and leaders to prepare as best we can for what the future will hold for ourselves and for our organizations.</p>
<p>As Seth Godin famously said: “Change almost never fails because it’s too early. It almost always fails because it’s too late.”</p>"""),

 dict(slug="episode-010-decentralized-leadership-with-dr-brian-smith",
  title="Episode #010: Decentralized Leadership with Dr. Brian Smith",
  date="April 10, 2022", cats="Podcast",
  desc="Episode #010 of the Fractional C-Suite Podcast discusses Decentralized Leadership with Dr. Brian Smith and Joe Frost.",
  img="https://josephmarkfrost.com/wp-content/uploads/2022/04/v01-FractionalCSuite-1024x1024.jpg",
  excerpt="An excellent discussion on decentralized leadership with Dr. Brian Smith, Founder of IA Business Advisors...",
  body="""<p>An excellent discussion on decentralized leadership with Dr. Brian Smith, Founder of IA Business Advisors, an internationally-recognized advisory, consulting and coaching firm. Brian has helped over 18,000 entrepreneurs, CEOs and teams across the globe. He is also the best-selling author of the “The I in Team” Series and most recently of the “Individual Advantages; Be the I in Team” books where he shares some of the best insights on creating great leaders and achieving true prosperity.</p>
<p>Listen to the full episode <a href="https://podcasts.apple.com/us/podcast/decentralized-leadership-fractional-c-suite-retreat/id1597847745?i=1000548936745">here</a>.</p>
<h3>Takeaways</h3>
<ul>
<li>The biggest opportunity for c-suites is getting in touch with what their company actually is. They need to be a few steps ahead of the curve.</li>
<li>Small businesses who struggle to afford someone at a c-suite level don’t have the same opportunities that those at the c-suite level know are possible.</li>
<li>A c-suite professional will look at things in the long term and not just what is going to happen in the next 30 days or 60 days. They will be a few cycles ahead of where you are now.</li>
<li>Decentralized leadership is where decision-making is delegated by top-level management to individuals within a company.</li>
<li>A fractional professional is a great advocate for changing things up. They will bring a new perspective to your business and can help you grow.</li>
<li>It’s a lot more cost effective for small companies to hire fractional professionals than it is to hire a full time c-suite executive.</li>
<li>It’s important when hiring someone to understand how they work by using an assessment like Kolbe. This will help you understand how they work and the best way to provide feedback to that employee.</li>
</ul>
<h3>Quote of the Show</h3>
<blockquote>1:30 – Dr. Brian Smith on decentralized leadership: “A lot of C-suite people have blinders on. They only see what’s in their lane and in the old days, we could almost do that. But the way that society has grown, the way that we’ve become a three dimensional society where we have to know more, we have to be more in touch, two or three steps away from ourselves.”</blockquote>"""),

 dict(slug="episode-009-partnering-for-success-with-nelson-tepfer",
  title="Episode #009: Partnering for Success with Nelson Tepfer",
  date="April 10, 2022", cats="Podcast",
  desc="Partnering for Success with Nelson Tepfer: what it takes to help a business increase its revenue by branching out.",
  img="https://josephmarkfrost.com/wp-content/uploads/2022/04/v01-FractionalCSuite-1024x1024.jpg",
  excerpt="In episode #009 of the “Fractional C-Suite Retreat” Podcast, I sat down with Nelson Tepfer, Managing Partner at ProCFO Partners...",
  body="""<p>In episode #009 of the “Fractional C-Suite Retreat” Podcast, I sat down with <a href="https://www.linkedin.com/in/tepfer/">Nelson Tepfer</a>, a Managing Partner at <a href="https://procfopartners.com/">ProCFO Partners</a>, to talk about partnering for success. He knows what it takes to help a business increase its revenue and isn’t afraid to branch out into different areas.</p>
<p>We spoke about some of the biggest innovations that C-suite leaders are looking at today.</p>
<p>Listen to the full episode <a href="https://podcasts.apple.com/us/podcast/partnering-for-success-fractional-c-suite-retreat-episode/id1597847745?i=1000548225065">here</a>.</p>
<h3>Takeaways</h3>
<ul>
<li>The biggest opportunity right now for c-suites is expanding beyond a traditional role and more collaboration with others.</li>
<li>Fractional professionals are great at rolling up their sleeves and doing the work that other full time c-suite executives are too busy for.</li>
<li>Bringing in a different perspective is one of the many positives about a fractional professional. They have worked with many different companies and know what strategies work and what doesn’t.</li>
<li>It is the CFO’s job to help the finance and accounting departments grow and they help build a framework for financial management.</li>
<li>There’s plenty of extra resources that a fractional professional can bring with them from company to company.</li>
<li>Always look for someone who is a fit with you as opposed to someone who’s been in your industry before.</li>
<li>Working with a company that has more CFOs can help develop a better process for your company.</li>
</ul>
<h3>Quote of the Show</h3>
<blockquote>20:03 – Nelson Tepfer on partnering for success: “Always look for someone who’s a fit with you, as opposed to somebody who’s been in your industry. I think that that is so crucial. From the client side, they just look at it as: if you haven’t been in this industry, how are you going to know certain aspects of this? The advantage to having a large team as we do have now more than 30 CFOs, we’ve been in just about every industry imaginable.”</blockquote>"""),
]

os.makedirs(os.path.join(OUT, "blog"), exist_ok=True)

# Post pages
for p in POSTS:
    page = post_page(p["title"], p["date"], p["cats"], p["body"] + BIO_4X if p["cats"] != "Podcast" else p["body"], p["desc"])
    with open(os.path.join(OUT, "blog", p["slug"] + ".html"), "w") as f:
        f.write(page)

# Blog index
cards = "\n".join(
    f'''<a class="post-card" href="{p['slug']}.html">
  <img src="{p['img']}" alt="">
  <div class="pad"><h3>{html.escape(p['title'])}</h3><p>{html.escape(p['excerpt'])}</p><p style="margin-top:10px;font-size:13px;color:var(--text-dim)">{p['date']} · {p['cats']}</p></div>
  <div class="more">Read More →</div>
</a>''' for p in POSTS)

index_body = f"""<section class="post-hero">
  <div class="wrap">
    <div class="kicker" style="color:var(--gold)">News, Podcast Episodes &amp; Insights by Joe</div>
    <h1>From the Blog</h1>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="post-grid">
{cards}
    </div>
  </div>
</section>"""

with open(os.path.join(OUT, "blog", "index.html"), "w") as f:
    f.write(SHELL.format(title="Blog", desc="News, podcast episodes and insights by Joe Frost on fractional and decentralized leadership.", body=index_body))

print("Built", len(POSTS), "posts + blog index")
