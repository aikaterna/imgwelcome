from .imgwelcome import ImgWelcome

def setup(bot):
	n = ImgWelcome(bot)
	bot.add_cog(n)
