_V='welcome.png'
_U='clear'
_T='TEXT_COLOR'
_S='SERVERTEXT_COLOR'
_R='OUTLINE_COLOR'
_Q='CIRCLE'
_P='BORDER_COLOR'
_O='BACKGROUND'
_N='I could not find that font file.'
_M='WELCOME_FONT_SIZE'
_L='WELCOME_FONT'
_K='SERVER_FONT_SIZE'
_J='SERVER_FONT'
_I='NAME_FONT_XSM'
_H='NAME_FONT_SM'
_G='NAME_FONT_MED'
_F='NAME_FONT_LG'
_E='NAME_FONT'
_D='RGBA'
_C=False
_B=None
_A=True
import asyncio,aiohttp,base64,datetime,discord,os,re
from redbot.core import Config,commands,checks
from redbot.core.data_manager import cog_data_path,bundled_data_path
from redbot.core.utils.chat_formatting import box,pagify
from io import BytesIO
from PIL import Image,ImageFont,ImageOps,ImageDraw
class ImgWelcome(commands.Cog):
	'Welcomes a user to the server with an image.'
	def __init__(A,bot):A.bot=bot;A.config=Config.get_conf(A,2713933330,force_registration=_A);A.datapath=str(cog_data_path(raw_name='ImgWelcome'));A.imgpath=str(bundled_data_path(A));B={'ANNOUNCE':_C,'ACCOUNT_WARNINGS':_A,_O:f"{A.imgpath}/transparent.png",_P:[255,255,255,230],'CHANNEL':_B,_Q:[128,128],_E:f"{A.imgpath}/fonts/UniSansHeavy.otf",_F:30,_G:22,_H:18,_I:12,_R:[0,0,0,255],_J:f"{A.imgpath}/fonts/UniSansHeavy.otf",_K:20,_S:[255,255,255,230],'SPECIAL_USERS':_A,_T:[255,255,255,230],_L:f"{A.imgpath}/fonts/UniSansHeavy.otf",_M:50};A.config.register_guild(**B);A.session=aiohttp.ClientSession();A.version='0.3.1'
	def cog_unload(A):A.bot.loop.create_task(A.session.close())
	async def _create_welcome(J,member,test_member_number:int=_B):
		w='of ';v='Welcome';u='L';U=test_member_number;D=member;A=await J.config.guild(D.guild).all();h=A[_L];i=A[_M];j=A[_J];k=A[_K];K=A[_E];l=A[_F];m=A[_G];n=A[_H];o=A[_I];V=ImageFont.truetype(h,i);L=ImageFont.truetype(j,k);W=ImageFont.truetype(K,l);X=ImageFont.truetype(K,m);Y=ImageFont.truetype(K,n);Z=ImageFont.truetype(K,o);a=Image.open(A[_O]).convert(_D);p=Image.open(J.imgpath+'/noimage.png');E=Image.new(_D,(500,150));E=ImageOps.fit(a,(500,150),centering=(0.5,0.5));E.paste(a);E=E.resize((500,150),Image.NEAREST);M=Image.new(u,(512,512),0);q=ImageDraw.Draw(M);q.ellipse(((0,0),(512,512)),fill=255);P=tuple(A[_Q]);M=M.resize(P,Image.ANTIALIAS)
		try:H=BytesIO();await D.avatar_url.save(H,seek_begin=_A);H=Image.open(H).convert(_D)
		except Exception as x:print('imgwelcome cog: {e}');H=p
		Q=ImageOps.fit(H,P,centering=(0,0));Q.putalpha(M);R=tuple(A[_P]);I=tuple(A[_T]);b=tuple(A[_S]);F=tuple(A[_R]);c=Image.new(u,(512,512),0);r=ImageDraw.Draw(c);r.ellipse((0,0)+(512,512),fill=255,outline=0);N=Image.new(_D,(512,512));s=ImageDraw.Draw(N);s.ellipse([0,0,512,512],fill=(R[0],R[1],R[2],180),outline=(255,255,255,250));O=await J._circle_border(P);N=N.resize(O,Image.ANTIALIAS);t=c.resize(O,Image.ANTIALIAS);d=7+int((136-O[0])/2);e=11+int((136-O[0])/2);C=ImageDraw.Draw(E);E.paste(N,(d,d),t);E.paste(Q,(e,e),Q);B=f"{str(D)}"
		def G(original_position,text,pixel_displacement,font,textoutline):E=textoutline;D=font;B=text;A=original_position;F=pixel_displacement;G=A[0]-F,A[1];H=A[0]+F,A[1];I=A[0],A[1]-F;J=A[0],A[1]+F;C.text(G,B,font=D,fill=E);C.text(H,B,font=D,fill=E);C.text(I,B,font=D,fill=E);C.text(J,B,font=D,fill=E);C.text(A,B,font=D,fill=E)
		G((150,16),v,1,V,F);C.text((150,16),v,font=V,fill=I)
		if len(B)<=17:G((152,63),B,1,W,F);C.text((152,63),B,font=W,fill=I)
		if len(B)>17:
			if len(B)<=23:G((152,66),B,1,X,F);C.text((152,66),B,font=X,fill=I)
		if len(B)>=24:
			if len(B)<=32:G((152,70),B,1,Y,F);C.text((152,70),B,font=Y,fill=I)
		if len(B)>=33:G((152,73),B,1,Z,F);C.text((152,73),B,font=Z,fill=I)
		if not U:S=sorted(D.guild.members,key=lambda m:m.joined_at).index(D)+1
		else:S=int(U)
		f=str(S)+J._get_suffix(S);g=str(D.guild.name)+'!'if len(str(D.guild.name))<=28 else str(D.guild.name)[:23]+'...';G((152,96),f"You are the {str(f)} member",1,L,F);C.text((152,96),f"You are the {str(f)} member",font=L,fill=b);G((152,116),w+g,1,L,F);C.text((152,116),w+g,font=L,fill=b);T=BytesIO();E.save(T,format='PNG');T.seek(0);return T
	async def _circle_border(C,circle_img_size:tuple):
		A=circle_img_size;B=[]
		for D in range(len(A)):B.append(A[0]+8)
		return tuple(B)
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
	async def imgwelcome(self,ctx):"Configuration options for the welcome image.\n        You must have server administrator perms or the bot's Admin or Mod role to use imgwelcome commands."
	@imgwelcome.command(name='border')
	@checks.mod_or_permissions(administrator=_A)
	async def imgwelcome_border(self,ctx,bordercolor=_B):
		'Set the profile image border color.\n        Use hex codes for colors and ‘clear’ for transparent.';C=bordercolor;B=ctx;A=self;E=230;D=_A
		if C==_U:await A.config.guild(B.guild).BORDER_COLOR.set([0,0,0,0])
		elif A._is_hex(C):await A.config.guild(B.guild).BORDER_COLOR.set(A._hex_to_rgb(C,E))
		else:await B.send('Border color is invalid. Use #000000 as a format.');D=_C
		if D:await B.send('The profile border color has been set.')
	@imgwelcome.command(name='channel')
	@checks.mod_or_permissions(administrator=_A)
	async def imgwelcome_channel(self,ctx,channel:discord.TextChannel):
		'Set the announcement channel.';B=channel;A=ctx
		if not A.guild.me.permissions_in(B).send_messages:return await A.send('No permissions to speak in that channel.')
		await self.config.guild(A.guild).CHANNEL.set(B.id);await B.send('This channel will be used for welcome messages.')
	@imgwelcome.command(name=_U)
	@checks.mod_or_permissions(administrator=_A)
	async def imgwelcome_clear(self,ctx):'Set the background to transparent.';await self.config.guild(ctx.guild).BACKGROUND.set(f"{self.imgpath}/transparent.png");await ctx.send('Welcome image background is now transparent.')
	@imgwelcome.command(name='outline')
	@checks.mod_or_permissions(administrator=_A)
	async def imgwelcome_outline(self,ctx,outline=_B):
		'Set the text outline. White or black.';B=outline;A=ctx;C=_A
		if B=='white':await self.config.guild(A.guild).OUTLINE_COLOR.set([255,255,255,255])
		elif B=='black':await self.config.guild(A.guild).OUTLINE_COLOR.set([0,0,0,255])
		else:await A.send('Outline color is invalid. Use white or black.');C=_C
		if C:await A.send('The text outline has been set.')
	@imgwelcome.command(name='preview')
	@checks.mod_or_permissions(administrator=_A)
	async def imgwelcome_preview(self,ctx,member:discord.Member=_B,number:int=_B):
		'Show a welcome image with the current settings.';A=member;C=ctx.message.channel
		if not A:A=ctx.author
		B=self.bot.get_channel(C.id);D=await self._create_welcome(A,number)
		async with B.typing():await B.send(file=discord.File(D,_V))
	@imgwelcome.command(name='size')
	@checks.mod_or_permissions(administrator=_A)
	async def imgwelcome_profilesize(self,ctx,profilesize:int):
		'Set the profile size in pixels. Use one number, 128 is recommended.';B=profilesize;A=ctx
		if B is 0:await A.send('Profile picture size must be larger than 0.');return
		else:await self.config.guild(A.guild).CIRCLE.set([B,B]);await A.send('The profile picture size has been set.')
	@imgwelcome.command(name='text')
	@checks.mod_or_permissions(administrator=_A)
	async def imgwelcome_text(self,ctx,textcolor:str, servercolor:str):
		'Set text colors. Use hex code for colors.';E=servercolor;D=textcolor;B=ctx;A=self;F=230;C=_A
		if A._is_hex(D):await A.config.guild(B.guild).TEXT_COLOR.set(A._hex_to_rgb(D,F))
		else:await B.send('Welcome text color is invalid. Use #000000 as a format.');C=_C
		if A._is_hex(E):await A.config.guild(B.guild).SERVERTEXT_COLOR.set(A._hex_to_rgb(E,F))
		else:await B.send('Server text color is invalid. Use #000000 as a format.');C=_C
		if C:await B.send('The text colors have been set.')
	@imgwelcome.command(name='toggle')
	@checks.mod_or_permissions(administrator=_A)
	async def imgwelcome_toggle(self,ctx):
		'Toggle welcome messages on the server.';B=self;A=ctx;C=await B.config.guild(A.guild).ANNOUNCE();D=await B.config.guild(A.guild).CHANNEL();await B.config.guild(A.guild).ANNOUNCE.set(not C)
		if not D:await B.config.guild(A.guild).CHANNEL.set(A.channel.id)
		if not C:await A.send('Now welcoming new users.')
		else:await A.send('No longer welcoming new users.')
	@imgwelcome.command(name='upload')
	@checks.mod_or_permissions(administrator=_A)
	async def imgwelcome_upload(self,ctx,default=_B):
		'Upload a background through Discord. 500px x 150px.\n        This must be an image file and not a url.';B=self;A=ctx;await A.send('Please send the file to use as a background. File must be 500px x 150px.')
		def F(m):return m.author==A.author
		try:
			G=await A.bot.wait_for('message',timeout=30.0,check=F)
			try:H=G.attachments[0].url;C=_A
			except IndexError:return await A.send('No image attachment in the last message. Try again later.')
		except asyncio.TimeoutError:C=_C;return await A.send('Try again later.')
		D=Image
		if C:
			try:
				async with B.session.get(H)as I:J=await I.content.read()
				if not os.path.exists(f"{B.datapath}/guilds/{A.guild.id}"):os.makedirs(f"{B.datapath}/guilds/{A.guild.id}")
				E=f"{B.datapath}/guilds/{A.guild.id}/serverbg.png"
				with open(E,'wb')as K:K.write(J);D=Image.open(E).convert(_D);C=_A
			except Exception as L:C=_C;print(L)
			if C:
				if D.size==(500,150):await B.config.guild(A.guild).BACKGROUND.set(f"{B.datapath}/guilds/{A.guild.id}/serverbg.png")
				else:return await A.send('Image needs to be 500x150.')
				M=f"{B.datapath}/guilds/{A.guild.id}/serverbg.png";await B.config.guild(A.guild).BACKGROUND.set(M);await A.send('Welcome image for this server set to uploaded file.')
			else:await A.send("Couldn't get the image from Discord.")
		else:await A.send("Couldn't get the image.")
	@imgwelcome.group(name='bonus')
	@checks.mod_or_permissions(administrator=_A)
	async def imgwelcome_bonus(self,ctx):'Toggle display of additional text welcome messages when a user joins the server.'
	@imgwelcome_bonus.command(name='user')
	@checks.mod_or_permissions(administrator=_A)
	async def bonus_user(self,ctx):
		'Toggle text announcement when a user is x 100th to join or #1337.';A=ctx;B=await self.config.guild(A.guild).SPECIAL_USERS();await self.config.guild(A.guild).SPECIAL_USERS.set(not B)
		if not B:await A.send('I will now announce when special users join.')
		else:await A.send('I will no longer announce when special users join.')
	@imgwelcome_bonus.command(name='warn')
	@checks.mod_or_permissions(administrator=_A)
	async def bonus_warn(self,ctx):
		"Toggle text announcement when a new user's account is <7d old.";A=ctx;B=await self.config.guild(A.guild).ACCOUNT_WARNINGS();await self.config.guild(A.guild).ACCOUNT_WARNINGS.set(not B)
		if not B:await A.send('I will now announce when new accounts join.')
		else:await A.send('I will no longer announce when new accounts join.')
	@imgwelcome.group(name='font',invoke_without_command=_A)
	@checks.mod_or_permissions(administrator=_A)
	async def imgwelcome_font(self,ctx):
		'Font settings.';C=self;B=ctx
		await B.send_help();A=await C.config.guild(B.guild).all();D=A[_E];E=A[_J];F=A[_L];D=await C._font_file(D);E=await C._font_file(E);F=await C._font_file(F);G='Current Font Settings:\n';G+=f"\n**Welcome Font**: {F[0]}.{F[1]} ({A['WELCOME_FONT_SIZE']}pt font)\n**Username Font**: {D[0]}.{D[1]} ({A['NAME_FONT_LG']}/{A['NAME_FONT_MED']}/{A['NAME_FONT_SM']}/{A['NAME_FONT_XSM']}pt font)\n**Member Position Font**: {E[0]}.{E[1]} ({A['SERVER_FONT_SIZE']}pt font)\n";H=discord.Embed(colour=await B.embed_colour(),description=G);await B.send(embed=H)
	@staticmethod
	async def _font_file(fontpath):'Return font names for the imgwelcome group command.';D='.';A=fontpath;B=A.split('/')[-1].split(D)[0];C=A.rsplit(D,1)[1];return B,C
	@imgwelcome_font.command(name='reset')
	@checks.mod_or_permissions(administrator=_A)
	async def fontg_reset(self,ctx):
		'Reset the fonts used and the font size back to default settings.\n           This command will not reset colors.';B=self
		async with B.config.guild(ctx.guild).all()as A:A[_E]=f"{B.imgpath}/fonts/UniSansHeavy.otf";A[_F]=30;A[_G]=22;A[_H]=18;A[_I]=12;A[_J]=f"{B.imgpath}/fonts/UniSansHeavy.otf";A[_K]=20;A[_L]=f"{B.imgpath}/fonts/UniSansHeavy.otf";A[_M]=50;await ctx.send('Default font and font sizes set.')
	@imgwelcome_font.command(name='list')
	@checks.mod_or_permissions(administrator=_A)
	async def fontg_list(self,ctx):
		'List fonts in the directory.';A=self;C=f"{A.imgpath}/fonts/";B=f"{A.datapath}/fonts/";F=os.listdir(C)
		try:D=os.listdir(B)
		except FileNotFoundError:os.mkdir(f"{A.datapath}/fonts/");D=os.listdir(B)
		G=sorted(F+D)
		if len(C)and len(B)==0:return await A.bot.send_message(channel,'No fonts found. Place fonts in your <data directory>/ImgWelcome/fonts/.')
		E='[Current fonts]\n'
		for H in G:E+=f"{H}\n"
		for I in pagify(E,delims=['\n']):await ctx.send(box(I,lang='ini'))
	@imgwelcome_font.command(name='name')
	@checks.mod_or_permissions(administrator=_A)
	async def fontg_name(self,ctx,font_name:str,size:int=_B):
		'Change the name text font.\n        e.g. [p]imgwelcome font name "UniSansHeavy.otf"\n        ';D=font_name;C=self;B=size;A=ctx;E=f"{C.datapath}/fonts/"
		if not B:B=await C.config.guild(A.guild).NAME_FONT_LG()
		try:ImageFont.truetype(E+D,B)
		except:await A.send(_N);return
		await C.config.guild(A.guild).NAME_FONT.set(E+D);await C.config.guild(A.guild).NAME_FONT_LG.set(B);await C.config.guild(A.guild).NAME_FONT_MED.set(B-8);await C.config.guild(A.guild).NAME_FONT_SM.set(B-12);await C.config.guild(A.guild).NAME_FONT_XSM.set(B-18);await A.send(f"Name font changed to: `{D}`, size: `{B}px`")
	@imgwelcome_font.command(name='server')
	@checks.mod_or_permissions(administrator=_A)
	async def fontg_server(self,ctx,font_name:str,size:int=_B):
		'Change the server text font.';D=font_name;C=self;B=size;A=ctx;E=f"{C.datapath}/fonts/"
		if not B:B=await C.config.guild(A.guild).SERVER_FONT_SIZE()
		try:ImageFont.truetype(E+D,B)
		except:return await A.send(_N)
		await C.config.guild(A.guild).SERVER_FONT.set(E+D);await C.config.guild(A.guild).SERVER_FONT_SIZE.set(B);await A.send(f"Server text font changed to: `{D}`, size: `{B}px`")
	@imgwelcome_font.command(name='welcome')
	@checks.mod_or_permissions(administrator=_A)
	async def fontg_welcome(self,ctx,font_name:str,size:int=_B):
		'Change the welcome text font.';D=font_name;C=self;B=size;A=ctx;E=f"{C.datapath}/fonts/"
		if not B:B=await C.config.guild(A.guild).WELCOME_FONT_SIZE()
		try:ImageFont.truetype(E+D,B)
		except:await A.send(_N);return
		await C.config.guild(A.guild).WELCOME_FONT.set(E+D);await C.config.guild(A.guild).WELCOME_FONT_SIZE.set(B);await A.send(f"Welcome font changed to: `{D}`, size: `{B}px`")
	@imgwelcome.command(name='version',hidden=_A)
	async def imgwelcomeset_version(self,ctx):'Displays the imgwelcome version.';A=base64.b64decode(b'VGhpcyBjb2cgaXMgb25seSBmb3IgUmVkLURpc2NvcmRCb3QgdjMu');A=A.decode('utf-8');await ctx.send(f"imgwelcome version {self.version}.\n{A}")
	@commands.Cog.listener()
	async def on_member_join(self,member):
		B=self;A=member;F=await B.config.guild(A.guild).ANNOUNCE()
		if not F:return
		G=await B.config.guild(A.guild).CHANNEL();C=B.bot.get_channel(G);H=await B._create_welcome(A)
		async with C.typing():await C.send(file=discord.File(H,_V))
		I=await B.config.guild(A.guild).SPECIAL_USERS()
		if(len(A.guild.members)%100==0 or len(A.guild.members)==1337)and I:J=f"Thanks {A.mention}, you're the ***{len(A.guild.members)}***th user on this server!";await C.send(J)
		K=datetime.datetime.strptime(str(A.created_at),'%Y-%m-%d %H:%M:%S.%f');D=datetime.datetime.now(datetime.timezone.utc);D=D.replace(tzinfo=_B);E=D-K;L=await B.config.guild(A.guild).ACCOUNT_WARNINGS()
		if E.days<7 and L:await C.send(f"This account was created less than a week ago ({E.days} days ago)")
