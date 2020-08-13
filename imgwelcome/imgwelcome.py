k='welcome.png'
j='clear'
AB='WELCOMETEXT_COLOR'
AA='SERVERTEXT_COLOR'
A9='OUTLINE_COLOR'
A8='CIRCLE'
A7='BORDER_COLOR'
A6='BACKGROUND'
A5=sorted
A4=Exception
R='I could not find that font file.'
p='TEXT_COLOR'
O=OSError
g='WELCOME_FONT_SIZE'
f='WELCOME_FONT'
e='SERVER_FONT_SIZE'
d='SERVER_FONT'
c='NAME_FONT_XSM'
b='NAME_FONT_SM'
a='NAME_FONT_MED'
Z='NAME_FONT_LG'
Y='NAME_FONT'
Q='RGBA'
J=tuple
I=int
H=False
E=None
D=len
B=str
A=True
import asyncio as S,aiohttp as T,base64 as U,datetime as N,discord as L,logging as V,os as K,re
from redbot.core import Config as W,commands as M,checks as C
from redbot.core.data_manager import cog_data_path as X,bundled_data_path as h
from redbot.core.utils.chat_formatting import box,pagify as i
from io import BytesIO as m
from PIL import Image as F,ImageFont as G,ImageOps as n,ImageDraw as P
o=V.getLogger('red.aikaterna.imgwelcome')
class ImgWelcome(M.Cog):
	'Welcomes a user to the server with an image.'
	def __init__(C,bot):C.bot=bot;C.config=W.get_conf(C,2751203330,force_registration=A);C.datapath=B(X(raw_name='ImgWelcome'));C.imgpath=B(h(C));D={'ANNOUNCE':H,'ACCOUNT_WARNINGS':A,A6:f"{C.imgpath}/transparent.png",A7:[255,255,255,230],'CHANNEL':E,A8:[128,128],Y:f"{C.imgpath}/fonts/UniSansHeavy.otf",Z:30,a:22,b:18,c:12,A9:[0,0,0,255],d:f"{C.imgpath}/fonts/UniSansHeavy.otf",e:20,AA:[255,255,255,230],'SPECIAL_USERS':A,p:[255,255,255,230],AB:E,f:f"{C.imgpath}/fonts/UniSansHeavy.otf",g:50};C.config.register_guild(**D);C.session=T.ClientSession();C.version='0.3.1'
	def cog_unload(A):A.bot.loop.create_task(A.session.close())
	async def _create_welcome(R,member,test_member_number:I=E):
		AQ='of ';AP='Welcome';q=test_member_number;K=member;C=await R.config.guild(K.guild).all();AC=C[f];AD=C[g];AE=C[d];AF=C[e];S=C[Y];AG=C[Z];AH=C[a];AI=C[b];AJ=C[c];r=G.truetype(AC,AD);T=G.truetype(AE,AF);s=G.truetype(S,AG);t=G.truetype(S,AH);u=G.truetype(S,AI);v=G.truetype(S,AJ);w=F.open(C[A6]).convert(Q);AK=F.open(R.imgpath+'/noimage.png');L=F.new(Q,(500,150));L=n.fit(w,(500,150),centering=(0.5,0.5));L.paste(w);L=L.resize((500,150),F.NEAREST);U=F.new('L',(512,512),0);AL=P.Draw(U);AL.ellipse(((0,0),(512,512)),fill=255);h=J(C[A8]);U=U.resize(h,F.ANTIALIAS)
		try:O=m();await K.avatar_url.save(O,seek_begin=A);O=F.open(O).convert(Q)
		except A4 as AR:o.error('ImgWelcome error in create_welcome:\n',exc_info=A);O=AK
		i=n.fit(O,h,centering=(0,0));i.putalpha(U);j=J(C[A7]);V=J(C[p]);x=J(C[AA])
		try:y=J(C[AB])
		except TypeError:y=J(C[p])
		M=J(C[A9]);z=F.new('L',(512,512),0);AM=P.Draw(z);AM.ellipse((0,0)+(512,512),fill=255,outline=0);W=F.new(Q,(512,512));AN=P.Draw(W);AN.ellipse([0,0,512,512],fill=(j[0],j[1],j[2],180),outline=(255,255,255,250));X=await R._circle_border(h);W=W.resize(X,F.ANTIALIAS);AO=z.resize(X,F.ANTIALIAS);A0=7+I((136-X[0])/2);A1=11+I((136-X[0])/2);H=P.Draw(L);L.paste(W,(A0,A0),AO);L.paste(i,(A1,A1),i);E=f"{B(K)}"
		def N(original_position:J,text:B,pixel_displacement:I,font,textoutline):D=textoutline;C=font;B=text;A=original_position;E=pixel_displacement;F=A[0]-E,A[1];G=A[0]+E,A[1];I=A[0],A[1]-E;J=A[0],A[1]+E;H.text(F,B,font=C,fill=D);H.text(G,B,font=C,fill=D);H.text(I,B,font=C,fill=D);H.text(J,B,font=C,fill=D);H.text(A,B,font=C,fill=D)
		N((150,16),AP,1,r,M);H.text((150,16),AP,font=r,fill=y)
		if D(E)<=17:N((152,63),E,1,s,M);H.text((152,63),E,font=s,fill=V)
		if D(E)>17:
			if D(E)<=23:N((152,66),E,1,t,M);H.text((152,66),E,font=t,fill=V)
		if D(E)>=24:
			if D(E)<=32:N((152,70),E,1,u,M);H.text((152,70),E,font=u,fill=V)
		if D(E)>=33:N((152,73),E,1,v,M);H.text((152,73),E,font=v,fill=V)
		if not q:k=A5(K.guild.members,key=lambda m:m.joined_at).index(K)+1
		else:k=I(q)
		A2=B(k)+R._get_suffix(k);A3=B(K.guild.name)+'!'if D(B(K.guild.name))<=28 else B(K.guild.name)[:23]+'...';N((152,96),f"You are the {B(A2)} member",1,T,M);H.text((152,96),f"You are the {B(A2)} member",font=T,fill=x);N((152,116),AQ+A3,1,T,M);H.text((152,116),AQ+A3,font=T,fill=x);l=m();L.save(l,format='PNG');l.seek(0);return l
	async def _circle_border(C,circle_img_size:J):
		A=circle_img_size;B=[]
		for E in range(D(A)):B.append(A[0]+8)
		return J(B)
	def _get_suffix(D,num):
		C='th';B={1:'st',2:'nd',3:'rd'}
		if 10<=num%100<=20:A=C
		else:A=B.get(num%10,C)
		return A
	def _hex_to_rgb(F,hex_num:B,a:I):
		A=hex_num.lstrip('#')
		if D(B(A))==3:E=''.join([C*2 for C in B(A)]);A=E
		C=[I(A[B:B+2],16)for B in(0,2,4)];C.append(a);return J(C)
	def _is_hex(F,color:B):
		A=color
		if A is not E and D(A)!=4 and D(A)!=7:return H
		C='^#(?:[0-9a-fA-F]{3}){1,2}$';return re.search(C,B(A))
	def _rgb_to_hex(B,rgb):A=rgb;A=J(A[:3]);return'#%02x%02x%02x'%A
	@M.guild_only()
	@M.group()
	async def imgwelcome(self,ctx):"Configuration options for the welcome image.\n        You must have server administrator perms or the bot's Admin or Mod role to use imgwelcome commands.";pass
	@imgwelcome.command(name='border')
	@C.mod_or_permissions(administrator=A)
	async def imgwelcome_border(self,ctx,bordercolor=E):
		'Set the profile image border color.\n        Use hex codes for colors and ‘clear’ for transparent.';D=bordercolor;C=ctx;B=self;F=230;E=A
		if D==j:await B.config.guild(C.guild).BORDER_COLOR.set([0,0,0,0])
		elif B._is_hex(D):await B.config.guild(C.guild).BORDER_COLOR.set(B._hex_to_rgb(D,F))
		else:await C.send('Border color is invalid. Use #000000 as a format.');E=H
		if E:await C.send('The profile border color has been set.')
	@imgwelcome.command(name='channel')
	@C.mod_or_permissions(administrator=A)
	async def imgwelcome_channel(self,ctx,channel:L.TextChannel):
		'Set the announcement channel.';B=channel;A=ctx
		if not A.guild.me.permissions_in(B).send_messages:return await A.send('No permissions to speak in that channel.')
		await self.config.guild(A.guild).CHANNEL.set(B.id);await B.send('This channel will be used for welcome messages.')
	@imgwelcome.command(name=j)
	@C.mod_or_permissions(administrator=A)
	async def imgwelcome_clear(self,ctx):'Set the background to transparent.';await self.config.guild(ctx.guild).BACKGROUND.set(f"{self.imgpath}/transparent.png");await ctx.send('Welcome image background is now transparent.')
	@imgwelcome.command(name='outline')
	@C.mod_or_permissions(administrator=A)
	async def imgwelcome_outline(self,ctx,outline=E):
		'Set the text outline. White or black.';C=outline;B=ctx;D=A
		if C=='white':await self.config.guild(B.guild).OUTLINE_COLOR.set([255,255,255,255])
		elif C=='black':await self.config.guild(B.guild).OUTLINE_COLOR.set([0,0,0,255])
		else:await B.send('Outline color is invalid. Use white or black.');D=H
		if D:await B.send('The text outline has been set.')
	@imgwelcome.command(name='preview')
	@C.mod_or_permissions(administrator=A)
	async def imgwelcome_preview(self,ctx,member:L.Member=E,number:I=E):
		'Show a welcome image with the current settings.';A=member;C=ctx.message.channel
		if not A:A=ctx.author
		B=self.bot.get_channel(C.id);D=await self._create_welcome(A,number)
		async with B.typing():await B.send(file=L.File(D,k))
	@imgwelcome.command(name='size')
	@C.mod_or_permissions(administrator=A)
	async def imgwelcome_profilesize(self,ctx,profilesize:I):
		'Set the profile size in pixels. Use one number, 128 is recommended.';B=profilesize;A=ctx
		if B==0:await A.send('Profile picture size must be larger than 0.');return
		else:await self.config.guild(A.guild).CIRCLE.set([B,B]);await A.send('The profile picture size has been set.')
	@imgwelcome.command(name='nametext')
	@C.mod_or_permissions(administrator=A)
	async def imgwelcome_nametext(self,ctx,name_text_color:B):
		'Set the name text color. Use hex code for color (#000000).';D=name_text_color;C=ctx;B=self;F=230;E=A
		if B._is_hex(D):await B.config.guild(C.guild).TEXT_COLOR.set(B._hex_to_rgb(D,F))
		else:await C.send('Name text color is invalid. Use #000000 as a format.');E=H
		if E:await C.send('The name text color has been set.')
	@imgwelcome.command(name='servertext')
	@C.mod_or_permissions(administrator=A)
	async def imgwelcome_servertext(self,ctx,server_text_color:B):
		'Set the server text color. Use hex code for color (#000000).';D=server_text_color;C=ctx;B=self;F=230;E=A
		if B._is_hex(D):await B.config.guild(C.guild).SERVERTEXT_COLOR.set(B._hex_to_rgb(D,F))
		else:await C.send('Server text color is invalid. Use #000000 as a format.');E=H
		if E:await C.send('The server text color has been set.')
	@imgwelcome.command(name='welcometext')
	@C.mod_or_permissions(administrator=A)
	async def imgwelcome_welcometext(self,ctx,welcome_text_color:B):
		'Set the welcome text color. Use hex code for color (#000000).';D=welcome_text_color;C=ctx;B=self;F=230;E=A
		if B._is_hex(D):await B.config.guild(C.guild).WELCOMETEXT_COLOR.set(B._hex_to_rgb(D,F))
		else:await C.send('Welcome text color is invalid. Use #000000 as a format.');E=H
		if E:await C.send('The welcome text color has been set.')
	@imgwelcome.command(name='toggle')
	@C.mod_or_permissions(administrator=A)
	async def imgwelcome_toggle(self,ctx):
		'Toggle welcome messages on the server.';B=self;A=ctx;C=await B.config.guild(A.guild).ANNOUNCE();D=await B.config.guild(A.guild).CHANNEL();await B.config.guild(A.guild).ANNOUNCE.set(not C)
		if not D:await B.config.guild(A.guild).CHANNEL.set(A.channel.id)
		if not C:await A.send('Now welcoming new users.')
		else:await A.send('No longer welcoming new users.')
	@imgwelcome.command(name='upload')
	@C.mod_or_permissions(administrator=A)
	async def imgwelcome_upload(self,ctx,default=E):
		'Upload a background through Discord. 500px x 150px.\n        This must be an image file and not a url.';C=self;B=ctx;await B.send('Please send the file to use as a background. File must be 500px x 150px.')
		def I(m):return m.author==B.author
		try:
			J=await B.bot.wait_for('message',timeout=30.0,check=I)
			try:L=J.attachments[0].url;D=A
			except IndexError:return await B.send('No image attachment in the last message. Try again later.')
		except S.TimeoutError:D=H;return await B.send('Try again later.')
		E=F
		if D:
			try:
				async with C.session.get(L)as M:N=await M.content.read()
				if not K.path.exists(f"{C.datapath}/guilds/{B.guild.id}"):K.makedirs(f"{C.datapath}/guilds/{B.guild.id}")
				G=f"{C.datapath}/guilds/{B.guild.id}/serverbg.png"
				with open(G,'wb')as O:O.write(N)
				E=F.open(G).convert(Q);D=A
			except A4 as R:D=H;o.error('ImgWelcome error in uploaded image:\n',exc_info=A)
			if D:
				if E.size==(500,150):await C.config.guild(B.guild).BACKGROUND.set(f"{C.datapath}/guilds/{B.guild.id}/serverbg.png")
				else:return await B.send('Image needs to be 500x150.')
				P=f"{C.datapath}/guilds/{B.guild.id}/serverbg.png";await C.config.guild(B.guild).BACKGROUND.set(P);await B.send('Welcome image for this server set to uploaded file.')
			else:await B.send("Couldn't get the image from Discord.")
		else:await B.send("Couldn't get the image.")
	@imgwelcome.group(name='bonus')
	@C.mod_or_permissions(administrator=A)
	async def imgwelcome_bonus(self,ctx):'Toggle display of additional text welcome messages when a user joins the server.';pass
	@imgwelcome_bonus.command(name='user')
	@C.mod_or_permissions(administrator=A)
	async def bonus_user(self,ctx):
		'Toggle text announcement when a user is x 100th to join or #1337.';A=ctx;B=await self.config.guild(A.guild).SPECIAL_USERS();await self.config.guild(A.guild).SPECIAL_USERS.set(not B)
		if not B:await A.send('I will now announce when special users join.')
		else:await A.send('I will no longer announce when special users join.')
	@imgwelcome_bonus.command(name='warn')
	@C.mod_or_permissions(administrator=A)
	async def bonus_warn(self,ctx):
		"Toggle text announcement when a new user's account is <7d old.";A=ctx;B=await self.config.guild(A.guild).ACCOUNT_WARNINGS();await self.config.guild(A.guild).ACCOUNT_WARNINGS.set(not B)
		if not B:await A.send('I will now announce when new accounts join.')
		else:await A.send('I will no longer announce when new accounts join.')
	@imgwelcome.group(name='font',autohelp=H)
	@C.mod_or_permissions(administrator=A)
	async def imgwelcome_font(self,ctx):
		'Font settings.';C=self;B=ctx
		if B.invoked_subcommand is E:await B.send_help();A=await C.config.guild(B.guild).all();D=A[Y];F=A[d];G=A[f];D=await C._font_file(D);F=await C._font_file(F);G=await C._font_file(G);H='Current Font Settings:\n';H+=f"\n**Welcome Font**: {G[0]}.{G[1]} ({A[g]}pt font)\n**Username Font**: {D[0]}.{D[1]} ({A[Z]}/{A[a]}/{A[b]}/{A[c]}pt font)\n**Member Position Font**: {F[0]}.{F[1]} ({A[e]}pt font)\n";I=L.Embed(colour=await B.embed_colour(),description=H);await B.send(embed=I)
	@staticmethod
	async def _font_file(fontpath):'Return font names for the imgwelcome group command.';D='.';A=fontpath;B=A.split('/')[-1].split(D)[0];C=A.rsplit(D,1)[1];return B,C
	@imgwelcome_font.command(name='reset')
	@C.mod_or_permissions(administrator=A)
	async def fontg_reset(self,ctx):
		'Reset the fonts used and the font size back to default settings.\n           This command will not reset colors.';B=self
		async with B.config.guild(ctx.guild).all()as A:A[Y]=f"{B.datapath}/fonts/UniSansHeavy.otf";A[Z]=30;A[a]=22;A[b]=18;A[c]=12;A[d]=f"{B.datapath}/fonts/UniSansHeavy.otf";A[e]=20;A[f]=f"{B.datapath}/fonts/UniSansHeavy.otf";A[g]=50;await ctx.send('Default font and font sizes set.')
	@imgwelcome_font.command(name='list')
	@C.mod_or_permissions(administrator=A)
	async def fontg_list(self,ctx):
		'List fonts in the directory.';A=self;C=f"{A.imgpath}/fonts/";B=f"{A.datapath}/fonts/";G=K.listdir(C)
		try:E=K.listdir(B)
		except FileNotFoundError:K.mkdir(f"{A.datapath}/fonts/");E=K.listdir(B)
		H=A5(list(set(G+E)))
		if D(C)and D(B)==0:return await A.bot.send_message(channel,'No fonts found. Place fonts in your <data directory>/ImgWelcome/fonts/.')
		F='[Current fonts]\n'
		for I in H:F+=f"{I}\n"
		for J in i(F,delims=['\n']):await ctx.send(box(J,lang='ini'))
	@imgwelcome_font.command(name='name')
	@C.mod_or_permissions(administrator=A)
	async def fontg_name(self,ctx,font_name:B,size:I=E):
		'Change the name text font.\n        e.g. [p]imgwelcome font name "UniSansHeavy.otf"\n        ';E=font_name;D=size;C=ctx;B=self;F=f"{B.datapath}/fonts/";I=f"{B.imgpath}/fonts/";J=H
		if not D:D=await B.config.guild(C.guild).NAME_FONT_LG()
		try:G.truetype(F+E,D)
		except O:
			try:G.truetype(I+E,D);J=A
			except:await C.send(R);return
		if not J:await B.config.guild(C.guild).NAME_FONT.set(F+E)
		else:await B.config.guild(C.guild).NAME_FONT.set(I+E)
		await B.config.guild(C.guild).NAME_FONT_LG.set(D);await B.config.guild(C.guild).NAME_FONT_MED.set(D-8);await B.config.guild(C.guild).NAME_FONT_SM.set(D-12);await B.config.guild(C.guild).NAME_FONT_XSM.set(D-18);await C.send(f"Name font changed to: `{E}`, size: `{D}px`")
	@imgwelcome_font.command(name='server')
	@C.mod_or_permissions(administrator=A)
	async def fontg_server(self,ctx,font_name:B,size:I=E):
		'Change the server text font.';E=font_name;D=size;C=ctx;B=self;F=f"{B.datapath}/fonts/";I=f"{B.imgpath}/fonts/";J=H
		if not D:D=await B.config.guild(C.guild).SERVER_FONT_SIZE()
		try:G.truetype(F+E,D)
		except O:
			try:G.truetype(I+E,D);J=A
			except:await C.send(R);return
		if not J:await B.config.guild(C.guild).SERVER_FONT.set(F+E)
		else:await B.config.guild(C.guild).SERVER_FONT.set(I+E)
		await B.config.guild(C.guild).SERVER_FONT_SIZE.set(D);await C.send(f"Server text font changed to: `{E}`, size: `{D}px`")
	@imgwelcome_font.command(name='welcome')
	@C.mod_or_permissions(administrator=A)
	async def fontg_welcome(self,ctx,font_name:B,size:I=E):
		'Change the welcome text font.';E=font_name;D=size;C=ctx;B=self;F=f"{B.datapath}/fonts/";I=f"{B.imgpath}/fonts/";J=H
		if not D:D=await B.config.guild(C.guild).WELCOME_FONT_SIZE()
		try:G.truetype(F+E,D)
		except O:
			try:G.truetype(I+E,D);J=A
			except:await C.send(R);return
		if not J:await B.config.guild(C.guild).WELCOME_FONT.set(F+E)
		else:await B.config.guild(C.guild).WELCOME_FONT.set(I+E)
		await B.config.guild(C.guild).WELCOME_FONT_SIZE.set(D);await C.send(f"Welcome font changed to: `{E}`, size: `{D}px`")
	@imgwelcome.command(name='version',hidden=A)
	async def imgwelcomeset_version(self,ctx):'Displays the imgwelcome version.';A=U.b64decode(b'VGhpcyBjb2cgaXMgb25seSBmb3IgUmVkLURpc2NvcmRCb3QgdjMu');A=A.decode('utf-8');await ctx.send(f"imgwelcome version {self.version}.\n{A}")
	@M.Cog.listener()
	async def on_member_join(self,member):
		C=self;A=member;I=await C.config.guild(A.guild).ANNOUNCE()
		if not I:return
		J=await C.config.guild(A.guild).CHANNEL();F=C.bot.get_channel(J);K=await C._create_welcome(A)
		async with F.typing():await F.send(file=L.File(K,k))
		M=await C.config.guild(A.guild).SPECIAL_USERS()
		if(D(A.guild.members)%100==0 or D(A.guild.members)==1337)and M:O=f"Thanks {A.mention}, you're the ***{D(A.guild.members)}***th user on this server!";await F.send(O)
		P=N.datetime.strptime(B(A.created_at),'%Y-%m-%d %H:%M:%S.%f');G=N.datetime.now(N.timezone.utc);G=G.replace(tzinfo=E);H=G-P;Q=await C.config.guild(A.guild).ACCOUNT_WARNINGS()
		if H.days<7 and Q:await F.send(f"This account was created less than a week ago ({H.days} days ago)")
