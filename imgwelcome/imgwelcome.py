_V='welcome.png'
_U='clear'
_T='TEXT_COLOR'
_S='SERVERTEXT_COLOR'
_R='OUTLINE_COLOR'
_Q='CIRCLE'
_P='BORDER_COLOR'
_O='BACKGROUND'
_N='I could not find that font file.'
_M='RGBA'
_L='WELCOME_FONT_SIZE'
_K='WELCOME_FONT'
_J='SERVER_FONT_SIZE'
_I='SERVER_FONT'
_H='NAME_FONT_XSM'
_G='NAME_FONT_SM'
_F='NAME_FONT_MED'
_E='NAME_FONT_LG'
_D='NAME_FONT'
_C=False
_B=None
_A=True
import asyncio,aiohttp,base64,datetime,discord,os,re
from redbot.core import Config,commands,checks
from redbot.core.data_manager import bundled_data_path
from io import BytesIO
from PIL import Image,ImageFont,ImageOps,ImageDraw
BaseCog=getattr(commands,'Cog',object)
class ImgWelcome(BaseCog):
	'Welcomes a user to the server with an image.'
	def __init__(A,bot):A.bot=bot;A.config=Config.get_conf(A,2751203330,force_registration=_A);B={'ANNOUNCE':_C,'ACCOUNT_WARNINGS':_A,_O:f"{bundled_data_path(A)}/transparent.png",_P:[255,255,255,230],'CHANNEL':_B,_Q:[128,128],_D:f"{bundled_data_path(A)}/fonts/UniSansHeavy.otf",_E:30,_F:22,_G:18,_H:12,_R:[0,0,0,255],_I:f"{bundled_data_path(A)}/fonts/UniSansHeavy.otf",_J:20,_S:[255,255,255,230],'SPECIAL_USERS':_A,_T:[255,255,255,230],_K:f"{bundled_data_path(A)}/fonts/UniSansHeavy.otf",_L:50};A.config.register_guild(**B);A.session=aiohttp.ClientSession();A.version='0.2.2'
	def __unload(A):A.session.detach()
	async def _create_welcome(H,member,url,test_member_number=_B):
		A1='of ';A0=' member';z='You are the ';y='Welcome';x='png';w='L';U=test_member_number;I=url;D=member;A=await H.config.guild(D.guild).all();i=A[_K];j=A[_L];k=A[_I];l=A[_J];K=A[_D];m=A[_E];n=A[_F];o=A[_G];p=A[_H];V=ImageFont.truetype(i,j);L=ImageFont.truetype(k,l);W=ImageFont.truetype(K,m);X=ImageFont.truetype(K,n);Y=ImageFont.truetype(K,o);Z=ImageFont.truetype(K,p);a=Image.open(A[_O]).convert(_M);q=Image.open(f"{bundled_data_path(H)}/noimage.png");E=Image.new(_M,(500,150));E=ImageOps.fit(a,(500,150),centering=(0.5,0.5));E.paste(a);E=E.resize((500,150),Image.NEAREST);M=Image.new(w,(512,512),0);r=ImageDraw.Draw(M);r.ellipse(((0,0),(512,512)),fill=255);P=tuple(A[_Q]);M=M.resize(P,Image.ANTIALIAS)
		try:I=I.replace('webp',x);I=I.replace('gif',x);await H._get_profile(I);b=Image.open(f"{bundled_data_path(H)}/profilepic.png")
		except Exception as s:print(f"Imgwelcome profile pic error: {s}");b=q
		Q=ImageOps.fit(b,P,centering=(0,0));Q.putalpha(M);R=tuple(A[_P]);J=tuple(A[_T]);c=tuple(A[_S]);F=tuple(A[_R]);d=Image.new(w,(512,512),0);t=ImageDraw.Draw(d);t.ellipse((0,0)+(512,512),fill=255,outline=0);N=Image.new(_M,(512,512));u=ImageDraw.Draw(N);u.ellipse([0,0,512,512],fill=(R[0],R[1],R[2],180),outline=(255,255,255,250));O=await H._circle_border(P);N=N.resize(O,Image.ANTIALIAS);v=d.resize(O,Image.ANTIALIAS);e=7+int((136-O[0])/2);f=11+int((136-O[0])/2);C=ImageDraw.Draw(E);E.paste(N,(e,e),v);E.paste(Q,(f,f),Q);B=str(D.name)+'#'+str(D.discriminator)
		def G(original_position,text,pixel_displacement,font,textoutline):E=textoutline;D=font;B=text;A=original_position;F=pixel_displacement;G=A[0]-F,A[1];H=A[0]+F,A[1];I=A[0],A[1]-F;J=A[0],A[1]+F;C.text(G,B,font=D,fill=E);C.text(H,B,font=D,fill=E);C.text(I,B,font=D,fill=E);C.text(J,B,font=D,fill=E);C.text(A,B,font=D,fill=E)
		G((150,16),y,1,V,F);C.text((150,16),y,font=V,fill=J)
		if len(B)<=17:G((152,63),B,1,W,F);C.text((152,63),B,font=W,fill=J)
		if len(B)>17:
			if len(B)<=23:G((152,66),B,1,X,F);C.text((152,66),B,font=X,fill=J)
		if len(B)>=24:
			if len(B)<=32:G((152,70),B,1,Y,F);C.text((152,70),B,font=Y,fill=J)
		if len(B)>=33:G((152,73),B,1,Z,F);C.text((152,73),B,font=Z,fill=J)
		if U is _B:S=sorted(D.guild.members,key=lambda m:m.joined_at).index(D)+1
		else:S=U
		g=str(S)+H._get_suffix(S);h=str(D.guild.name)+'!'if len(str(D.guild.name))<=28 else str(D.guild.name)[:23]+'...';G((152,96),z+str(g)+A0,1,L,F);C.text((152,96),z+str(g)+A0,font=L,fill=c);G((152,116),A1+h,1,L,F);C.text((152,116),A1+h,font=L,fill=c);T=BytesIO();E.save(T,format='PNG');T.seek(0);return T
	async def _circle_border(C,circle_img_size):
		A=circle_img_size;B=[]
		for D in range(len(A)):B.append(A[0]+8)
		return tuple(B)
	async def _get_profile(A,url):
		async with A.session.get(url)as B:C=await B.content.read()
		with open(f"{bundled_data_path(A)}/profilepic.png",'wb')as D:D.write(C)
	def _get_suffix(D,num):
		C='th';B={1:'st',2:'nd',3:'rd'}
		if 10<=num%100<=20:A=C
		else:A=B.get(num%10,C)
		return A
	def _hex_to_rgb(D,hex_num,a):
		A=hex_num.lstrip('#')
		if len(str(A))==3:C=''.join([B*2 for B in(str(A))]);A=C
		B=[int(A[B:B+2],16)for B in((0,2,4))];B.append(a);return tuple(B)
	def _is_hex(C,color):
		A=color
		if A is not _B and len(A)!=4 and len(A)!=7:return _C
		B='^#(?:[0-9a-fA-F]{3}){1,2}$';return re.search(B,str(A))
	def _rgb_to_hex(B,rgb):A=rgb;A=tuple(A[:3]);return'#%02x%02x%02x'%A
	@commands.guild_only()
	@commands.group()
	async def imgwelcome(self,ctx):'Configuration options for the welcome image.'
	@checks.admin_or_permissions(manage_guild=_A)
	@imgwelcome.command(name='border')
	async def imgwelcome_border(self,ctx,bordercolor=_B):
		'Set the profile image border color.\n        Use hex codes for colors and ‘clear’ for transparent.';C=bordercolor;B=ctx;A=self;E=230;D=_A
		if C==_U:await A.config.guild(B.guild).BORDER_COLOR.set([0,0,0,0])
		elif A._is_hex(C):await A.config.guild(B.guild).BORDER_COLOR.set(A._hex_to_rgb(C,E))
		else:await B.send('Border color is invalid. Use #000000 as a format.');D=_C
		if D:await B.send('The profile border color has been set.')
	@checks.admin_or_permissions(manage_guild=_A)
	@imgwelcome.command(name='channel')
	async def imgwelcome_channel(self,ctx,channel):
		'Set the announcement channel.';B=channel;A=ctx
		if not A.guild.me.permissions_in(B).send_messages:return await A.send('No permissions to speak in that channel.')
		await self.config.guild(A.guild).CHANNEL.set(B.id);await B.send('This channel will be used for welcome messages.')
	@checks.admin_or_permissions(manage_guild=_A)
	@imgwelcome.command(name=_U)
	async def imgwelcome_clear(self,ctx):'Set the background to transparent.';await self.config.guild(ctx.guild).BACKGROUND.set(f"{bundled_data_path(self)}/transparent.png");await ctx.send('Welcome image background is now transparent.')
	@checks.admin_or_permissions(manage_guild=_A)
	@imgwelcome.command(name='outline')
	async def imgwelcome_outline(self,ctx,outline=_B):
		'Set the text outline. White or black.';B=outline;A=ctx;C=_A
		if B=='white':await self.config.guild(A.guild).OUTLINE_COLOR.set([255,255,255,255])
		elif B=='black':await self.config.guild(A.guild).OUTLINE_COLOR.set([0,0,0,255])
		else:await A.send('Outline color is invalid. Use white or black.');C=_C
		if C:await A.send('The text outline has been set.')
	@checks.admin_or_permissions(manage_guild=_A)
	@imgwelcome.command(name='preview')
	async def imgwelcome_preview(self,ctx,member=_B,number=_B):
		'Show a welcome image with the current settings.';A=member;C=ctx.message.channel
		if A is _B:A=ctx.author
		B=self.bot.get_channel(C.id);D=await self._create_welcome(A,A.avatar_url,number)
		async with B.typing():await B.send(file=discord.File(D,_V))
	@checks.admin_or_permissions(manage_guild=_A)
	@imgwelcome.command(name='size')
	async def imgwelcome_profilesize(self,ctx,profilesize):
		'Set the profile size in pixels. Use one number, 128 is recommended.';B=profilesize;A=ctx
		if B is 0:await A.send('Profile picture size must be larger than 0.');return
		else:await self.config.guild(A.guild).CIRCLE.set([B,B]);await A.send('The profile picture size has been set.')
	@checks.admin_or_permissions(manage_guild=_A)
	@imgwelcome.command(name='text')
	async def imgwelcome_text(self,ctx,textcolor,servercolor):
		'Set text colors. Use hex code for colors.';E=servercolor;D=textcolor;B=ctx;A=self;F=230;C=_A
		if A._is_hex(D):await A.config.guild(B.guild).TEXT_COLOR.set(A._hex_to_rgb(D,F))
		else:await B.send('Welcome text color is invalid. Use #000000 as a format.');C=_C
		if A._is_hex(E):await A.config.guild(B.guild).SERVERTEXT_COLOR.set(A._hex_to_rgb(E,F))
		else:await B.send('Server text color is invalid. Use #000000 as a format.');C=_C
		if C:await B.send('The text colors have been set.')
	@checks.admin_or_permissions(manage_guild=_A)
	@imgwelcome.command(name='toggle')
	async def imgwelcome_toggle(self,ctx):
		'Toggle welcome messages on the server.';B=self;A=ctx;C=await B.config.guild(A.guild).ANNOUNCE();D=await B.config.guild(A.guild).CHANNEL();await B.config.guild(A.guild).ANNOUNCE.set(not C)
		if not D:await B.config.guild(A.guild).CHANNEL.set(A.channel.id)
		if not C:await A.send('Now welcoming new users.')
		else:await A.send('No longer welcoming new users.')
	@checks.admin_or_permissions(manage_guild=_A)
	@imgwelcome.command(name='upload')
	async def imgwelcome_upload(self,ctx,default=_B):
		'Upload a background through Discord. 500px x 150px.\n        This must be an image file and not a url.';B=self;A=ctx;await A.send('Please send the file to use as a background. File must be 500px x 150px.')
		def F(m):return m.author==A.author
		try:G=await A.bot.wait_for('message',timeout=30.0,check=F);H=G.attachments[0].url;C=_A
		except asyncio.TimeoutError:C=_C;return await A.send('Try again later.')
		D=Image
		if C:
			try:
				async with B.session.get(H)as I:J=await I.content.read()
				if not os.path.exists(f"{bundled_data_path(B)}/{A.guild.id}"):os.makedirs(f"{bundled_data_path(B)}/{A.guild.id}")
				E=f"{bundled_data_path(B)}/{A.guild.id}/serverbg.png"
				with open(E,'wb')as K:K.write(J);D=Image.open(E).convert(_M);C=_A
			except Exception as L:C=_C;print(f"Imgwelcome file error: {L}")
			if C:
				if D.size==(500,150):await B.config.guild(A.guild).BACKGROUND.set(f"{bundled_data_path(B)}/{A.guild.id}/serverbg.png")
				else:return await A.send('Image needs to be 500x150.')
				M=f"{bundled_data_path(B)}/{A.guild.id}/serverbg.png";await B.config.guild(A.guild).BACKGROUND.set(M);await A.send('Welcome image for this server set to uploaded file.')
			else:await A.send("Couldn't get the image from Discord.")
		else:await A.send("Couldn't get the image.")
	@checks.admin_or_permissions(manage_guild=_A)
	@imgwelcome.group(name='bonus')
	async def imgwelcome_bonus(self,ctx):'Toggle display of additional text welcome messages when a user joins the server.'
	@checks.admin_or_permissions(manage_guild=_A)
	@imgwelcome_bonus.command(name='user')
	async def bonus_user(self,ctx):
		'Toggle text announcement when a user is x 100th to join or #1337.';A=ctx;B=await self.config.guild(A.guild).SPECIAL_USERS();await self.config.guild(A.guild).SPECIAL_USERS.set(not B)
		if not B:await A.send('I will now announce when special users join.')
		else:await A.send('I will no longer announce when special users join.')
	@checks.admin_or_permissions(manage_guild=_A)
	@imgwelcome_bonus.command(name='warn')
	async def bonus_warn(self,ctx):
		"Toggle text announcement when a new user's account is <7d old.";A=ctx;B=await self.config.guild(A.guild).ACCOUNT_WARNINGS();await self.config.guild(A.guild).ACCOUNT_WARNINGS.set(not B)
		if not B:await A.send('I will now announce when new accounts join.')
		else:await A.send('I will no longer announce when new accounts join.')
	@checks.admin_or_permissions(manage_guild=_A)
	@imgwelcome.group(name='font',autohelp=_C)
	async def imgwelcome_font(self,ctx):
		'Font settings.';C=self;B=ctx
		if str(B.invoked_subcommand)=='imgwelcome font':await B.send_help();A=await C.config.guild(B.guild).all();D=A[_D];E=A[_I];F=A[_K];D=await C._font_file(D);E=await C._font_file(E);F=await C._font_file(F);G='Current Font Settings:\n';G+=f"\n**Welcome Font**: {F[0]}.{F[1]} ({A['WELCOME_FONT_SIZE']}pt font)\n**Username Font**: {D[0]}.{D[1]} ({A['NAME_FONT_LG']}/{A['NAME_FONT_MED']}/{A['NAME_FONT_SM']}/{A['NAME_FONT_XSM']}pt font)\n**Member Position Font**: {E[0]}.{E[1]} ({A['SERVER_FONT_SIZE']}pt font)\n";H=discord.Embed(colour=await B.embed_colour(),description=G);await B.send(embed=H)
	@staticmethod
	async def _font_file(fontpath):'Return font names for the imgwelcome group command.';D='.';A=fontpath;B=A.split('/')[-1].split(D)[0];C=A.rsplit(D,1)[1];return B,C
	@checks.admin_or_permissions(manage_guild=_A)
	@imgwelcome_font.command(name='reset')
	async def fontg_reset(self,ctx):
		'Reset the fonts used and the font size back to default settings.\n           This command will not reset colors.';B=self
		async with B.config.guild(ctx.guild).all()as A:A[_D]=f"{bundled_data_path(B)}/fonts/UniSansHeavy.otf";A[_E]=30;A[_F]=22;A[_G]=18;A[_H]=12;A[_I]=f"{bundled_data_path(B)}/fonts/UniSansHeavy.otf";A[_J]=20;A[_K]=f"{bundled_data_path(B)}/fonts/UniSansHeavy.otf";A[_L]=50;await ctx.send('Default font and font sizes set.')
	@checks.admin_or_permissions(manage_guild=_A)
	@imgwelcome_font.command(name='list')
	async def fontg_list(self,ctx):
		'List fonts in the directory.';F='```';C=f"{bundled_data_path(self)}/fonts/";B=sorted(os.listdir(C))
		if len(B)==0:await self.bot.send_message(channel,'No fonts found. Place fonts in your data dir/imgwelcome/fonts/.');return
		A=commands.formatter.Paginator(prefix=F,suffix=F,max_size=2000);A.add_line('Current fonts:')
		for D in B:A.add_line(D)
		for E in A.pages:await ctx.send(E)
	@checks.admin_or_permissions(manage_guild=_A)
	@imgwelcome_font.command(name='name')
	async def fontg_name(self,ctx,font_name,size=_B):
		'Change the name text font.\n        e.g. [p]imgwelcome font name "UniSansHeavy.otf"\n        ';D=font_name;C=size;B=self;A=ctx;E=f"{bundled_data_path(B)}/fonts/"
		if C is _B:C=await B.config.guild(A.guild).NAME_FONT_LG()
		try:ImageFont.truetype(E+D,C)
		except:await A.send(_N);return
		await B.config.guild(A.guild).NAME_FONT.set(E+D);await B.config.guild(A.guild).NAME_FONT_LG.set(C);await B.config.guild(A.guild).NAME_FONT_MED.set(C-8);await B.config.guild(A.guild).NAME_FONT_SM.set(C-12);await B.config.guild(A.guild).NAME_FONT_XSM.set(C-18);await A.send(f"Name font changed to: {D}")
	@checks.admin_or_permissions(manage_guild=_A)
	@imgwelcome_font.command(name='server')
	async def fontg_server(self,ctx,font_name,size=_B):
		'Change the server text font.';D=font_name;C=size;B=self;A=ctx;E=f"{bundled_data_path(B)}/fonts/"
		if C is _B:C=await B.config.guild(A.guild).SERVER_FONT_SIZE()
		try:ImageFont.truetype(E+D,C)
		except:return await A.send(_N)
		await B.config.guild(A.guild).SERVER_FONT.set(E+D);await B.config.guild(A.guild).SERVER_FONT_SIZE.set(C);await A.send(f"Server text font changed to: {D}")
	@checks.admin_or_permissions(manage_guild=_A)
	@imgwelcome_font.command(name='welcome')
	async def fontg_welcome(self,ctx,font_name,size=_B):
		'Change the welcome text font.';D=font_name;C=size;B=self;A=ctx;E=f"{bundled_data_path(B)}/fonts/"
		if C is _B:C=await B.config.guild(A.guild).WELCOME_FONT_SIZE()
		try:ImageFont.truetype(E+D,C)
		except:await A.send(_N);return
		await B.config.guild(A.guild).WELCOME_FONT.set(E+D);await B.config.guild(A.guild).WELCOME_FONT_SIZE.set(C);await A.send(f"Welcome font changed to: {D}")
	@imgwelcome.command(name='version',hidden=_A)
	async def imgwelcomeset_version(self,ctx):'Displays the imgwelcome version.';A=base64.b64decode(b'VGhpcyBjb2cgaXMgb25seSBmb3IgUmVkLURpc2NvcmRCb3QgdjMu');A=A.decode('utf-8');await ctx.send(f"imgwelcome version {self.version}.\n{A}")
	async def on_member_join(B,member):
		A=member;F=await B.config.guild(A.guild).ANNOUNCE()
		if not F:return
		G=await B.config.guild(A.guild).CHANNEL();C=B.bot.get_channel(G);H=await B._create_welcome(A,A.avatar_url)
		async with C.typing():await C.send(file=discord.File(H,_V))
		I=await B.config.guild(A.guild).SPECIAL_USERS()
		if(len(A.guild.members)%100==0 or len(A.guild.members)==1337)and I:J=f"Thanks {A.mention}, you're the ***{len(A.guild.members)}***th user on this server!";await C.send(J)
		K=datetime.datetime.strptime(str(A.created_at),'%Y-%m-%d %H:%M:%S.%f');D=datetime.datetime.now(datetime.timezone.utc);D=D.replace(tzinfo=_B);E=D-K;L=await B.config.guild(A.guild).ACCOUNT_WARNINGS()
		if E.days<7 and L:await C.send(f"This account was created less than a week ago ({E.days} days ago)")
