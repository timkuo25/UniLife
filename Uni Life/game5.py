import pygame
import time
import pickle

pygame.init()

pygame.font.get_fonts()

red = (255,0,0)
white = (255,255,255)
black = (0,0,0)
bright_black = (50, 50, 50)
bright_gray = (209, 209, 209)
dark_gray = (143,143,143)

screen_width = 1280
screen_height = 720

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('testing game')
pygame.display.update()

clock = pygame.time.Clock()

#crowdtalk_sound = pygame.mixer.Sound('talk_cut.wav')


font = pygame.font.SysFont('mingliupmingliumingliuhkscs',20)
font_for_title = pygame.font.SysFont('mingliupmingliumingliuhkscs',25)
#font_for_opening = pygame.font.SysFont('mingliupmingliumingliuhkscs',25)

theblock_for_changing_background = 6
	
def message_to_screen(msg,color,x,y):
	screen_text = font.render(msg,True,color)
	screen.blit(screen_text,[x,y])
	
	
def message_to_screen_for_title(msg,color,x,y):
	screen_text = font_for_title.render(msg,True,color)
	screen.blit(screen_text,[x,y])
	
def show_text_name_for_2(textforname):
	message_to_screen_for_title(textforname,black,130,477)
	pygame.display.update()
	
def show_text_name_for_4(textforname):
	#姓和名中間要加3個block
	message_to_screen_for_title(textforname,black,80,477)
	pygame.display.update()
	
def show_text_1(text1):
	message_to_screen(text1,black,55,580)
	pygame.display.update()
	
def show_text_2(text2):
	message_to_screen(text2,black,55,612)
	pygame.display.update()
	
def show_text_3(text3):
	message_to_screen(text3,black,55,644)
	pygame.display.update()
	
def show_text_4(text4):
	message_to_screen(text4,black,55,676)
	pygame.display.update()
	
def original_board(bg):
	global background_file, background
	background_file = bg
	background = pygame.image.load(background_file).convert()
	screen.blit(background, (0, 0))
	pygame.display.update()
	
class two_background(pygame.sprite.Sprite):
	
	def __init__(self, screen, nowback, newback):
		pygame.sprite.Sprite.__init__(self)
		
		self.pre_background = nowback
		self.des_background = newback
		
		self.preback = pygame.image.load(self.pre_background)
		self.preback = self.preback.convert()
		self.desback = pygame.image.load(self.des_background)
		self.desback = self.desback.convert()
		
		self.images = [self.preback, self.desback]
		self.image = self.images[0]
		self.rect = self.image.get_rect()
		self.screen = screen
		
		self.i = 0
		
	def update(self):
		self.rect.centerx = (screen_width / 2)
		self.rect.centery = (screen_height / 2)
		self.image = self.images[self.i]

		
		

class CrossFade(pygame.sprite.Sprite):
	
	def __init__(self, screen):
		pygame.sprite.Sprite.__init__(self)
		
		self.image = pygame.Surface(screen.get_size())
		self.image = self.image.convert()
		#self.image.fill((0, 0, 0))
		
		self.rect = self.image.get_rect()
		
		self.fade_dir = 1
		
		self.trans_value = 0
		
		self.fade_speed = 6
		
		self.delay = 1
		
		self.image.set_alpha(self.trans_value)
		
		self.rect.centerx = screen_width / 2
		self.rect.centery = screen_height / 2
		
	def update(self):
		self.image.set_alpha(self.trans_value)	
		
		if self.fade_dir > 0:
				
			if self.trans_value - self.fade_speed < 0:
				self.trans_value = 0
			else:
				self.trans_value -= self.fade_speed
					
					
		elif self.fade_dir < 0:
				
			if self.trans_value + self.delay > 225:
				self.trans_value = 225
			else:
				self.trans_value += self.fade_speed


def change_background(now, new, changespeed):
	global screen, background
	
	fade = CrossFade(screen)

	back_surface = two_background(screen,now, new)
	
	all_Sprites = pygame.sprite.OrderedUpdates(back_surface, fade)
	
	havebeenfaded = False
	havebeenchanged = False
	
	
			
			
	while not havebeenchanged:
		clock.tick(60)
		pygame.time.delay(changespeed)
		
		if fade.trans_value == 0:
			fade.fade_dir *= -1
			
		all_Sprites.clear(screen, background)
		all_Sprites.update()
		all_Sprites.draw(screen)
		if fade.trans_value == 225:
			back_surface.i = 1
			fade.fade_dir = 1
			all_Sprites.clear(screen, background)
			all_Sprites.update()
			all_Sprites.draw(screen)
			havebeenfaded = True
		if fade.trans_value == 0 and havebeenfaded == True:
			havebeenchanged = True
			#return theblock_for_changing_background
			
		pygame.display.flip()



def saving():
	global x, par, chapter_pointer, musicfrom, goch1, goch2, goch3, data, background_file, gameExit, nowplaying, playmusic1,playmusic1_2, playmusic2, playmusic3, playmusic4, play_ed
	
	saved = False
	while not saved:
		pygame.draw.rect(screen, black, [200, 50, 700, 70])
		message_to_screen("WHICH FILE DO YOU WANT TO SAVE THE GAME?(1/2/3)", white, 210, 70)
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					saved = True
				if event.key == pygame.K_1:
					musicfrom += float(pygame.mixer.music.get_pos() / 1000)
					data = [x, par, chapter_pointer, musicfrom, goch1, goch2, goch3, background_file, nowplaying, playmusic, playmusic2]
					with open("saved1", "wb") as f:
						pickle.dump(data, f)
						f.close()
						saved = True
				if event.key == pygame.K_2:
					musicfrom += float(pygame.mixer.music.get_pos() / 1000)
					data = [x, par, chapter_pointer, musicfrom, goch1, goch2, goch3, background_file, nowplaying, playmusic, playmusic2]
					with open("saved2", "wb") as f:
						pickle.dump(data, f)
						f.close()
						saved = True
				if event.key == pygame.K_3:
					musicfrom += float(pygame.mixer.music.get_pos() / 1000)
					data = [x, par, chapter_pointer, musicfrom, goch1, goch2, goch3, background_file, nowplaying, playmusic, playmusic2]
					with open("saved3", "wb") as f:
						pickle.dump(data, f)
						f.close()
						saved = True
	
	gameExit = True			
	
	
def loading():
	global x, par, chapter_pointer, musicfrom, goch1, goch2, goch3, data, background_file, gameExit, nowplaying, playmusic1,playmusic1_2, playmusic2, playmusic3, playmusic4, play_ed, loaded
	
	original_board(background_file)
	
	loaded = False	
	while not loaded:
		#global x, par, chapter_pointer, musicfrom, goch1, goch2, goch3, data, background_file
		
		#clock.tick(60)

		
		#pygame.draw.rect(screen, black, [540, 400, 200, 50], 5)
		message_to_screen_for_title("NEW GAME",black,590,412.5)
		
		#pygame.draw.rect(screen, black, [540, 480, 200, 50], 5)
		message_to_screen_for_title("DATA1",black,610,492.5)
		
		#pygame.draw.rect(screen, black, [540, 560, 200, 50], 5)
		message_to_screen_for_title("DATA2",black,610,572.5)
		
		#pygame.draw.rect(screen, black, [540, 640, 200, 50], 5)
		message_to_screen_for_title("DATA3",black,610,652.5)
		#pygame.display.flip()	
		
		if loaded == False:
			button_for_intro(540, 400, 200, 50, 5, bright_gray, dark_gray, "NEW GAME")
		if loaded == False:
			button_for_intro(540, 480, 200, 50, 5, bright_gray, dark_gray, "DATA1")
		if loaded == False:
			button_for_intro(540, 560, 200, 50, 5, bright_gray, dark_gray, "DATA2")
		if loaded == False:
			button_for_intro(540, 640, 200, 50, 5, bright_gray, dark_gray, "DATA3")
		
		
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_n:	
					loaded = True
					change_background("start.png", "第一章.png", 20)
					background_file = "第一章.png"
				
				if event.key == pygame.K_1:	
					with open("saved1", "rb") as f:
						data = pickle.load(f)						
					x = data[0]
					par = data[1]
					chapter_pointer = data[2]
					musicfrom = data[3]
					goch1 = data[4]
					goch2 = data[5]
					goch3 = data[6]
					background_file = data[7]
					nowplaying = data[8]
					playmusic = data[9]
					playmusic2 = data[10]
					loaded = True
					change_background("start.png", background_file, 20)
					
				if event.key == pygame.K_2:
					with open("saved2", "rb") as f:
						data = pickle.load(f)							
					x = data[0]
					par = data[1]
					chapter_pointer = data[2]
					musicfrom = data[3]
					goch1 = data[4]
					goch2 = data[5]
					goch3 = data[6]
					background_file = data[7]
					nowplaying = data[8]
					playmusic = data[9]
					playmusic2 = data[10]
					loaded = True
					change_background("start.png", background_file, 20)
					
				if event.key == pygame.K_3:
					with open("saved3", "rb") as f:
						data = pickle.load(f)									
					x = data[0]
					par = data[1]
					chapter_pointer = data[2]
					musicfrom = data[3]
					goch1 = data[4]
					goch2 = data[5]
					goch3 = data[6]
					background_file = data[7]
					nowplaying = data[8]
					playmusic = data[9]
					playmusic2 = data[10]
					loaded = True
					change_background("start.png", background_file, 20)
			

def button_for_intro(x_pos, y, w, h, line_thickness, ic, ac, whattodo = None):
	global x, par, chapter_pointer, musicfrom, goch1, goch2, goch3, data, background_file, gameExit, nowplaying, playmusic1,playmusic1_2, playmusic2, playmusic3, playmusic4, play_ed, loaded
	
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	
	if x_pos < mouse[0] < x_pos + w and y < mouse[1] < y + h:
		pygame.draw.rect(screen, ac, [x_pos, y, w, h], line_thickness)
		if click[0] == 1 and whattodo != None:
			if whattodo == "NEW GAME":
				loaded = True
				change_background("start.png", "第一章.png", 20)
				background_file = "第一章.png"
			elif whattodo == "DATA1":
				with open("saved1", "rb") as f:
						data = pickle.load(f)						
				x = data[0]
				par = data[1]
				chapter_pointer = data[2]
				musicfrom = data[3]
				goch1 = data[4]
				goch2 = data[5]
				goch3 = data[6]
				background_file = data[7]
				nowplaying = data[8]
				playmusic = data[9]
				playmusic2 = data[10]
				loaded = True
				change_background("start.png", background_file, 20)
			elif whattodo == "DATA2":
				with open("saved2", "rb") as f:
						data = pickle.load(f)							
				x = data[0]
				par = data[1]
				chapter_pointer = data[2]
				musicfrom = data[3]
				goch1 = data[4]
				goch2 = data[5]
				goch3 = data[6]
				background_file = data[7]
				nowplaying = data[8]
				playmusic = data[9]
				playmusic2 = data[10]
				loaded = True
				change_background("start.png", background_file, 20)
			elif whattodo == "DATA3":
				with open("saved3", "rb") as f:
						data = pickle.load(f)									
				x = data[0]
				par = data[1]
				chapter_pointer = data[2]
				musicfrom = data[3]
				goch1 = data[4]
				goch2 = data[5]
				goch3 = data[6]
				background_file = data[7]
				nowplaying = data[8]
				playmusic = data[9]
				playmusic2 = data[10]
				loaded = True
				change_background("start.png", background_file, 20)
				
	else:
		pygame.draw.rect(screen, ic, [x_pos, y, w, h], line_thickness)
		
	
	pygame.display.flip()	



def button_for_chapter(msg, x_pos, y, w, h, line_thickness, ic, ac, whattodo = None):
	global x, par, chapter_pointer, musicfrom, goch1, goch2, goch3, data, background_file, gameExit, nowplaying, playmusic1,playmusic1_2, playmusic2, playmusic3, playmusic4, play_ed, loaded, choice, z
	
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	
	message_to_screen(msg, black, x_pos + 20, y + 5)
	
	if x_pos < mouse[0] < x_pos + w and y < mouse[1] < y + h:
		pygame.draw.rect(screen, ac, [x_pos, y, w, h], line_thickness)
		if click[0] == 1 and whattodo != None:
			if whattodo == "兩位關係真不錯，我在這都沒認識的人哈哈":
				choice = 1
				z = 1
			elif whattodo == "真假，為什麼不用客氣啊，客氣不好嗎==":
				choice = 2
				z = 1
			elif whattodo == "那他講幹話的時候我嗆爆妳可以嗎":
				choice = 3
				z = 1
			
			elif whattodo == "剛好沒甚麼事，就出去逛逛吧":
				choice = 1
				z = 1
			elif whattodo == "在宿舍讀書好了":
				choice = 2
				z = 1
			
			elif whattodo == "會回家":
				choice = 1
				z = 1
			elif whattodo == "不回家":
				choice = 2
				z = 1
			
			elif whattodo == "我需要治療！":
				z = 1
				
			
			elif whattodo == "物歸原位(丟回去)":
				choice = 1
				z = 1
			elif whattodo == "先收著":
				choice = 2
				z = 1
			elif whattodo == "PO學校交流板":
				choice = 3
				z = 1
				
			elif whattodo == "參加":
				choice = 1
				z = 1
			
			elif whattodo == "出發":
				choice = 1
				z = 1	
	
	
	else:
		pygame.draw.rect(screen, ic, [x_pos, y, w, h], line_thickness)
		
	
	pygame.display.flip()	
	
	
	
def chapter_1():
	global x, goch1, par, theblock_for_changing_background,playmusic1, playmusic1_2, playmusic2, nowplaying, musicfrom, choice, z
	
	if par == 0:
		original_board("第一章.png")
		pygame.time.delay(1500)
		original_board("第一章.png")
		change_background("第一章.png", "黒+對話框.png", 30)
		par += 1
	
	
	elif par == 1:
		theblock_for_changing_background = 12 + 1
		
		if playmusic1 == True:
			pygame.mixer.music.fadeout(1000)
			pygame.mixer.music.load("kara_m01.mp3")
			musicfrom = 0
			nowplaying = "kara_m01.mp3"
			pygame.mixer.music.play(-1)	
			playmusic1 = False
			
		if x == 0:
			original_board("黒+對話框.png")
		elif x == 1:
			show_text_1("曾幾何時，我們睜開眼不再做夢，夢只能隱晦的收藏？")
		elif x == 2:
			show_text_2("曾幾何時，空白筆記填滿的是數學公式，而非一條蛇吞了大象？")
		elif x == 3:
			show_text_3("我不是我，我是一張張成績單。專心讀書，進好大學出社會，當個成功的人，幸福就會不請自來。")
		elif x == 4:
			show_text_4("大人是這樣說的，所以我這樣做。")
		elif x == 5:
			original_board("黒+對話框.png")
			x += 1
		elif x == 6:
			show_text_1("我們都被豢養，所以不需要飛翔。")
		elif x == 7:
			show_text_2("18歲了，如果考得不好，我應該負責嗎？")
		elif x == 8:
			show_text_3("進大學了，我需要負責嗎？")
		elif x == 9:
			show_text_4("這是我的選擇嗎？")
		elif x == 10:
			original_board("黒+對話框.png")
		elif x == 11:
			show_text_1("說得好像我有得選一樣。")
		elif x == 12:
			change_background("黒+對話框.png", "校園+對話框.png", 30)
			par += 1
			x = 0
	
	
	

	elif par == 2:
		theblock_for_changing_background = 20 + 1
		if x == 0:
			original_board("校園+對話框.png")
		elif x == 1:
			show_text_1("開學典禮")
		elif x == 2:
			original_board("校園+對話框+名字框.png")
			#pygame.mixer.Sound.play(crowdtalk_sound)
		elif x == 3:
			show_text_name_for_2("校長")
		elif x == 4:
			show_text_1("歡迎來到柏勞大學！")
		elif x == 5:
			show_text_2("在這令人興奮的時刻，我在台上看到的是一朵朵生機盎然的嫩芽，渴望著養分灌溉。")
		elif x == 6:
			show_text_3("本校是何其榮幸，能做為孕育優秀如你們的搖籃。")
		elif x == 7:
			show_text_4("從收到入學通知書的那一刻起，你們就代表了本校，和本校的未來。")
		elif x == 8:
			original_board("校園+對話框+名字框.png")
			x += 1
		elif x == 9:
			show_text_name_for_2("校長")
			show_text_1("今日你以勞大為榮，他日勞大將以你為榮，恭喜各位！")
		elif x == 10:
			original_board("校園+對話框+名字框.png")
			x += 1
		elif x == 11:
			show_text_name_for_2("校長")
		elif x == 12:
			show_text_1("我們來自不同的地方，有著不同的背景，一個人的際遇造就了現在的自己，而我們現在齊聚在這裡。")
		elif x == 13:
			show_text_2("你們想成為怎麼樣的人呢？我期待你們能在這階段結交好友，成就自己。")
		elif x == 14:
			show_text_3("你也許會困惑，你一定會遇到困難，但請記得你並不是一個人。")
		elif x == 15:
			original_board("校園+對話框+名字框.png")
			x += 1
		elif x == 16:
			show_text_name_for_2("校長")
		elif x == 17:
			show_text_1("大學是各位一生至關重要的階段，一個人的選擇，編織了一段段不同的人生，串聯起一篇篇精彩的故事。")
		elif x == 18:
			show_text_2("請尊重引導你們的師長，謹言慎行、服從校規。")
		elif x == 19:
			show_text_3("當你們面臨進行重大抉擇的時刻，請務必慎重，並為自己的選擇負起責任。")
		elif x == 20:
			original_board("校園+對話框.png")
			par += 1
			x = 0
			
	elif par == 3:
		theblock_for_changing_background = 5 + 1
		if x == 0:
			original_board("校園+對話框.png")
		elif x == 1:
			show_text_1("所有校長都有的共通點，廢話特多，而且都是老爺爺。校長上台開講已經有20分鐘，感覺還要一陣子。")
		elif x == 2:
			show_text_2("大部分的學生都已經沒有耐心聽演講，有些開始滑手機，有些開始和身邊的人搭訕自我介紹。")
		elif x == 3:
			show_text_3("入學第一天除了參加入學典禮也沒有其他事情會發生。我百無聊賴地拿出手機滑了起來。")
		elif x == 4:
			show_text_4("(開學典禮結束)")
		elif x == 5:
			change_background("校園+對話框.png", "教室+對話框.png", 30)
			par += 1
			x = 0
			
			
			
	elif par == 4:
		theblock_for_changing_background = 7 + 1
		if x == 0:
			original_board("教室+對話框.png")
		elif x == 1:
			show_text_1("（第一堂課）")
		elif x == 2:
			original_board("教室+對話框.png")
		elif x == 3:
			show_text_1("第一堂課，周圍坐的系上同學大約也有上百位...我們真算是一個大系，想到要記起這上百人的名字，就覺得寧願去背英文單字。。")
		elif x == 4:
			show_text_2("教室是個階梯式講堂，高中時也只有在大一點的特殊教室或補習班才看的到這種形式。")
		elif x == 5:
			show_text_3("雖然人數眾多，教室內的氣氛大致是低迷的，只有少數互相認識的人低聲交談。")
		elif x == 6:
			show_text_4("這時多少會覺得要是身旁有個認識的人就好了…我亂講的，被認出來多尷尬==")
		elif x == 7:
			change_background("教室+對話框.png", "教室+對話框+名字框.png", 30)
			par += 1
			x = 0
			
			
	elif par == 5:
		theblock_for_changing_background = 10 + 1
		if x == 0:
			original_board("教室+對話框+名字框.png")
		elif x == 1:
			show_text_name_for_2("教授")
			show_text_1("啊嗯~同學們請安靜坐好，開始上課囉")
		elif x == 2:
			original_board("教室+對話框.png")
		elif x == 3:
			show_text_1("拈著陰柔的聲線，看起來年約五六十的教授走進教室，身材有些臃腫。")
		elif x == 4:
			show_text_2("偏圓的臉，黝黑的肌膚和所剩不多的白髮訴說著歲月，但並不影響他的意氣風發。")
		elif x == 5:
			original_board("教室+對話框+名字框.png")
			x += 1
		elif x == 6:
			show_text_name_for_2("教授")
		elif x == 7:
			show_text_1("還是不免俗地說一句歡迎各位來到柏勞大學。在剛脫離升學壓力，迎接新生活的階段，我明白大家都還是很亢奮的。")
		elif x == 8:
			show_text_2("但也要勸各位盡早收起浮躁，好好努力才是真的。")
		elif x == 9:
			show_text_3("教授在大學時代，大家都在辦活動在玩的時候，我總是一個人在圖書館．．．．．．")
		elif x == 10:
			original_board("教室+對話框.png")
			par += 1
			x = 0
			
			
	elif par == 6:
		theblock_for_changing_background = 8 + 1
		if x == 0:
			original_board("教室+對話框.png")
		elif x == 1:
			show_text_1("教授開始說起當年他是如何寒窗十年無人問、取得今日規模的成就、羨煞多少浮世眾生．．．．．．")
		elif x == 2:
			show_text_2("又扯一些什麼沒實力就等淘汰啊、什麼人脈很重要啊、眼光放遠才能獲得最大利益等等等等。")
		elif x == 3:
			original_board("教室+對話框.png")
			x += 1
		elif x == 4:
			show_text_1("天啊，管院的人都這樣嗎？")
		elif x == 5:
			show_text_2("我以後會變得和他一樣嗎？")
		elif x == 6:
			show_text_3("不好吧==")
		elif x == 7:
			show_text_4("現在回頭太遲了嗎？")
		elif x == 8:
			original_board("教室+對話框+名字框.png")
			par += 1
			x = 0
			
	elif par == 7:
		theblock_for_changing_background = 4 + 1
		if x == 0:
			original_board("教室+對話框+名字框.png")
			x += 1
		elif x == 1:
			show_text_name_for_2("教授")
		elif x == 2:
			show_text_1("．．．．．．以後進了職場，一個重要的能力就是和人群說話，那就是我們今天要做的事啦。")
		elif x == 3:
			show_text_2("請大家上台用一分鐘介紹你自己，下次再開始上正課。")
		elif x == 4:
			original_board("教室+對話框.png")
			par += 1
			x = 0
			
	elif par == 8:
		theblock_for_changing_background = 5 + 1
		if x == 0:
			original_board("教室+對話框.png")
			x += 1
		elif x == 1:
			show_text_1("教授拿出事先護貝好的名牌，讓大家能看清楚接下來上台的人的名字。")
		elif x == 2:
			show_text_2("第一堂課就是上百人一個一個自我介紹，")
		elif x == 3:
			show_text_3("這種方式雖然對認識人沒什麼幫助，但似乎也沒有更好的方法了。")
		elif x == 4:
			show_text_4("一開始大家都還試著掰出一分鐘的長度，後來漸漸地大家就開始無視這規則了......而我也是這麼打算的。")
		elif x == 5:
			change_background("教室+對話框.png", "教室+對話框+名字框.png", 10)
			par += 1
			x = 0
	
	
	elif par == 9:
		theblock_for_changing_background = 6 + 1
		if x == 0:
			original_board("教室+對話框+名字框.png")
		elif x == 1:
			show_text_name_for_4("御影   翔平")
			show_text_1("我叫御影翔平，希望能和大家好好相處，請多指教。")
		elif x == 2:
			original_board("教室+對話框.png")
		elif x == 3:
			show_text_1("台下響起些微意思性的掌聲送我回到座位，")
		elif x == 4:
			show_text_2("正當我想繼續滑手機時，")
		elif x == 5:
			show_text_3("後方傳來一句男聲。")
		elif x == 6:
			change_background("教室+對話框.png", "教室+好朋友+對話框+名字框.png", 30)
			par += 1
			x = 0
	
	elif par == 10:
		theblock_for_changing_background = 8 + 1
		if x == 0:
			original_board("教室+好朋友+對話框+名字框.png")
		elif x == 1:
			show_text_name_for_2("??")
			show_text_1("這堂課還真奇怪，對吧？")
		elif x == 2:
			original_board("教室+好朋友+對話框.png")
		elif x == 3:
			show_text_1("回頭一看，一個戴著粗框眼鏡的帥氣男孩笑咪咪地看著我。")
		elif x == 4:
			original_board("教室+好朋友+對話框+名字框.png")
		elif x == 5:
			show_text_name_for_2("??")
			show_text_1("我叫神谷智則，御影同學，請多指教。")
		elif x == 6:
			original_board("教室+好朋友+對話框+名字框.png")
		elif x == 7:
			show_text_name_for_4("御影   翔平")
			show_text_1("喔喔嗨，很高興認識你。")
		elif x == 8:
			change_background("教室+好朋友+對話框+名字框.png", "教室+對話框.png", 30)
			par += 1
			x = 0
			
			
	elif par == 11:
		theblock_for_changing_background = 3 + 1
		if x == 0:
			original_board("教室+對話框.png")
		elif x == 1:
			show_text_1("智則他看起來就是那種幽默開朗，大家看到都會喜歡的那種人。")
		elif x == 2:
			show_text_2("可能只是想找個人聊天吧...")
		elif x == 3:
			change_background("教室+對話框.png", "教室+好朋友+對話框+名字框.png", 30)
			par += 1
			x = 0
			
			
			
	elif par == 12:
		theblock_for_changing_background = 21 + 1
		if x == 0:
			original_board("教室+好朋友+對話框+名字框.png")
		elif x == 1:
			show_text_name_for_4("神谷   智則")
			show_text_1("聽我學長說，這教授是我們的鎮系之寶，他有一大堆傳奇故事，讓同學們一屆一屆的傳頌下去。")
		elif x == 2:
			original_board("教室+好朋友+對話框+名字框.png")
		elif x == 3:
			show_text_name_for_4("御影   翔平")
			show_text_1("是喔，像是什麼？")
		elif x == 4:
			original_board("教室+好朋友+對話框+名字框.png")
		elif x == 5:
			show_text_name_for_4("神谷   智則")
			show_text_1("像是人人看到他都得堆滿笑臉的和他打招呼，從前不和他講話的系花看到他就會給個大大的擁抱之類的。")
		elif x == 6:
			original_board("教室+好朋友+對話框+名字框.png")
		elif x == 7:
			show_text_name_for_4("御影   翔平")
			show_text_1("太有錢了吧==，有地位就是任性耶，是不是該出門找工作了啊？")
		elif x == 8:
			original_board("教室+好朋友+對話框+名字框.png")
		elif x == 9:
			show_text_name_for_4("神谷   智則")
			show_text_1("他每屆會選某些「可愛」的學生給予特別的「照顧」，")
		elif x == 10:
			show_text_2("聽說他還單獨請學姐吃過冰淇淋呢，那可是人人稱羨的待遇喔！")
		elif x == 11:
			original_board("教室+好朋友+對話框+名字框.png")
		elif x == 12:
			show_text_name_for_4("御影   翔平")
			show_text_1("天啊好羨慕喔，那教授會不會傳裸照啊？好想看喔==")
		elif x == 13:
			original_board("教室+好朋友+對話框+名字框.png")
		elif x == 14:
			show_text_name_for_4("神谷   智則")
			show_text_1("什麼鬼哈哈哈")
		elif x == 15:
			show_text_2("聽說這學校畢業生的就業率是完美的100%，而且他們全都進入了很不錯的大公司呢")
		elif x == 16:
			original_board("教室+好朋友+對話框+名字框.png")
		elif x == 17:
			show_text_name_for_4("御影   翔平")
			show_text_1("這樣啊，我想大家都是一樣看上這點拼命考進來的吧。")
		elif x == 18:
			original_board("教室+好朋友+對話框+名字框.png")
		elif x == 19:
			show_text_name_for_4("神谷   智則")
			show_text_1("對阿，大家都希望能順利畢業並成功就業。")
		elif x == 20:
			show_text_2("對了你看，現在在台上的是我朋友。")
		elif x == 21:
			change_background("教室+好朋友+對話框+名字框.png", "教室+女主+對話框.png", 30)
			par += 1
			x = 0
			
			
	elif par == 13:
		theblock_for_changing_background = 4 + 1
		if x == 0:
			original_board("教室+女主+對話框.png")
		elif x == 1:
			show_text_1("現在在台上的女生，名字叫榊原凜。")
		elif x == 2:
			show_text_2("說話有點小聲，卻是堅定的那種，給人一種無法忽視的感覺。")
		elif x == 3:
			show_text_3("介紹完後，她朝我們這邊走過來。")
		elif x == 4:
			change_background("教室+女主+對話框.png", "教室+好朋友和女主+對話框+名字框.png", 30)
			par += 1
			x = 0
			
	elif par == 14:		
		theblock_for_changing_background = 14 + 1
		if x == 0:
			original_board("教室+好朋友和女主+對話框+名字框.png")	
		elif x == 1:
			show_text_name_for_4("神谷   智則")
			show_text_1("辛苦囉，這位是御影翔平，交個朋友吧～")
		elif x == 2:
			original_board("教室+好朋友和女主+對話框+名字框.png")
			x += 1
		elif x == 3:
			show_text_name_for_4("御影   翔平")
			show_text_1("哈囉哈囉~")
		elif x == 4:
			original_board("教室+好朋友和女主+對話框+名字框.png")
			x += 1
		elif x == 5:
			show_text_name_for_4("榊原   凜")
			show_text_1("嗨，智則應該沒太騷擾你吧")
		elif x == 6:
			original_board("教室+好朋友和女主+對話框+名字框.png")
		elif x == 7:
			show_text_name_for_4("神谷   智則")
			show_text_1("我們高中同班，算老友了吧。她現在單身，目標好像是一學期交一個男友的樣子。")
		elif x == 8:
			original_board("教室+好朋友和女主+對話框+名字框.png")
		elif x == 9:
			show_text_name_for_4("榊原   凜")
			show_text_1("跟你考上同系真衰哈哈，你不要玩到被當再來找我求救就好。")
		elif x == 10:
			show_text_2("翔平，要是以後智則跟你講什麼幹話你就嗆爆他不用客氣xD")
		elif x == 11:
			original_board("教室+好朋友和女主+對話框+名字框.png")
			x += 1
		elif x == 12:
			show_text_name_for_4("御影   翔平")
		elif x == 13:
			button_for_chapter("兩位關係真不錯，我在這都沒認識的人哈哈",100, 580, 800, 30, 2, dark_gray, black, whattodo = "兩位關係真不錯，我在這都沒認識的人哈哈")
			button_for_chapter("真假，為什麼不用客氣啊，客氣不好嗎==", 100, 620, 800, 30, 2, dark_gray, black, whattodo = "真假，為什麼不用客氣啊，客氣不好嗎==")
			button_for_chapter("那他講幹話的時候我嗆爆妳可以嗎", 100, 660, 800, 30, 2, dark_gray, black, whattodo = "那他講幹話的時候我嗆爆妳可以嗎")
		if x > 13:
			x = 13
		if z == 1:
			change_background("教室+好朋友和女主+對話框+名字框.png", "教室+好朋友和女主+對話框+名字框.png", 30)
			par += 1
			x = 0
			
			
	elif par == 15 and choice == 1:
		theblock_for_changing_background = 4 + 1
		z = 0
		if x == 0:
			original_board("教室+好朋友和女主+對話框+名字框.png")	
		elif x == 1:
			show_text_name_for_4("榊原   凜")
			show_text_1("沒事，以後有事可以找我們，沒事也可以。")
		elif x == 2:
			original_board("教室+好朋友和女主+對話框+名字框.png")
		elif x == 3:
			show_text_name_for_4("神谷   智則")
			show_text_1("我覺得不行。")
		elif x == 4:
			change_background("教室+好朋友和女主+對話框+名字框.png", "教室+對話框.png", 30)
			par += 1
			x = 0
			
			
	elif par == 15 and choice == 2:
		theblock_for_changing_background = 8 + 1
		z = 0
		if x == 0:
			original_board("教室+好朋友和女主+對話框+名字框.png")
		elif x == 1:
			show_text_name_for_4("榊原   凜")
			show_text_1("對齁，有道理欸！你邏輯是不是還不錯啊==")
		elif x == 2:
			original_board("教室+好朋友和女主+對話框+名字框.png")
		elif x == 3:
			show_text_name_for_4("御影   翔平")
			show_text_1("還好啦，就if跟else而已啊~")
		elif x == 4:
			original_board("教室+好朋友和女主+對話框+名字框.png")
		elif x == 5:
			show_text_name_for_4("神谷   智則")
			show_text_1("對啊，這樣就停修也太玻璃了吧")
		elif x == 6:
			original_board("教室+好朋友和女主+對話框+名字框.png")
		elif x == 7:
			show_text_name_for_2("三人")
			show_text_1("哈哈哈哈哈哈哈哈哈哈")
		elif x == 8:
			change_background("教室+好朋友和女主+對話框+名字框.png", "教室+對話框.png", 30)
			par += 1
			x = 0
			
			
	elif par == 15 and choice == 3:
		theblock_for_changing_background = 4 + 1
		z = 0
		if x == 0:
			original_board("教室+好朋友和女主+對話框+名字框.png")
		elif x == 1:
			show_text_name_for_4("榊原   凜")
			show_text_1("好問題欸，等，我想一下==")
		elif x == 2:
			original_board("教室+好朋友和女主+對話框+名字框.png")
		elif x == 3:
			show_text_name_for_4("神谷   智則")
			show_text_1("哇塞，你把在場所有人都嗆過一遍也沒問題吧？")
		elif x == 4:
			change_background("教室+好朋友和女主+對話框+名字框.png", "教室+對話框.png", 30)
			par += 1
			x = 0
			
			
	elif par == 16:
		theblock_for_changing_background = 5 + 1
		choice = 0
		if x == 0:
			original_board("教室+對話框.png")
		elif x == 1:
			show_text_1("簡單聊了幾句...")
		elif x == 2:
			show_text_2("姑且算是認識了兩位同學吧")
		elif x == 3:
			show_text_3("超乎預期的多呢。")
		elif x == 4:
			show_text_4("（第一堂課結束）")
		elif x == 5:
			change_background("教室+對話框.png", "黒+對話框.png", 30)
			par += 1
			x = 0

			
	elif par == 17:
		theblock_for_changing_background = 9 + 1
		
		if playmusic1_2 == True:
			pygame.mixer.music.fadeout(1000)
			pygame.mixer.music.load("one_days_leave.mp3")
			musicfrom = 0
			nowplaying = "one_days_leave.mp3"
			pygame.mixer.music.play(-1)	
			playmusic1_2 = False
			
			
		if x == 0:
			original_board("黒+對話框.png")
		elif x == 1:
			show_text_1("(過了一些日子)")
		elif x == 2:
			original_board("黒+對話框.png")
		elif x == 3:
			show_text_1("原以為上了大學脫離家裡，生活會改變許多。")			
		elif x == 4:
			show_text_2("其實也真的還好，或許個性上我就是比較獨立吧。")
		elif x == 5:
			original_board("黒+對話框.png")
		elif x == 6:
			show_text_1("不管怎麼樣，開學也快一個月了，差不多習慣了這裡的生活，")
		elif x == 7:
			original_board("黒+對話框.png")
		elif x == 8:
			show_text_1("系上的氣氛也漸漸活絡起來了。")
		elif x == 9:
			change_background("黒+對話框.png", "街頭+好朋友+對話框+名字框.png", 30)
			par += 1
			x = 0
			
	elif par == 18:	
		theblock_for_changing_background = 7 + 1
		if x == 0:
			original_board("街頭+好朋友+對話框+名字框.png")
		elif x == 1:
			show_text_name_for_4("神谷   智則")
			show_text_1("周末有空嗎？要不要一起出去逛逛？")
		elif x == 2:
			original_board("街頭+好朋友+對話框.png")
		elif x == 3:
			show_text_1("開學以來多少也記住了幾位同學的名字，不過比較常往來的還是只有智則和凜。")
		elif x == 4:
			original_board("街頭+好朋友+對話框.png")
		elif x == 5:
			show_text_1("智則是熱情的人，不過…該去嗎？")
		elif x == 6:
			original_board("街頭+好朋友+對話框.png")
		elif x == 7:
			button_for_chapter("剛好沒甚麼事，就出去逛逛吧",100, 580, 800, 30, 2, dark_gray, black, whattodo = "剛好沒甚麼事，就出去逛逛吧")
			button_for_chapter("在宿舍讀書好了", 100, 620, 800, 30, 2, dark_gray, black, whattodo = "在宿舍讀書好了")
		if x > 7:
			x = 7
		if z == 1:
			change_background("街頭+好朋友+對話框.png", "街頭+好朋友+對話框+名字框.png", 30)
			par += 1
			x = 0
			
			
	elif par == 19 and choice == 1:	
		theblock_for_changing_background = 4 + 1
		z = 0
		if x == 0:
			original_board("街頭+好朋友+對話框+名字框.png")
		elif x == 1:
			show_text_name_for_4("神谷   智則")
			show_text_1("耐斯，那就到時候見囉！")
		elif x == 2:
			original_board("街頭+對話框.png")
		elif x == 3:
			show_text_1("要拒絕他還真有點不好意思，現在也沒什麼心情念書，出去散散心也好吧。")
		elif x == 4:
			change_background("街頭+對話框.png", "第二章.png", 30)
			par += 1
			x = 0
			
	elif par == 19 and choice == 2:	
		theblock_for_changing_background = 33 + 1
		z = 0
		if x == 0:
			original_board("街頭+好朋友+對話框+名字框.png")
		elif x == 1:
			show_text_name_for_4("神谷   智則")
			show_text_1("好吧，我好像也應該讀點書……")
		elif x == 2:
			original_board("街頭+好朋友+對話框+名字框.png")
		elif x == 3:
			show_text_name_for_4("神谷   智則")
			show_text_1("沒有啦，我亂講的== 改天有空一起出來吧。")
		elif x == 4:
			original_board("街頭+對話框.png")
		elif x == 5:
			show_text_1("其實拒絕他還滿不好意思的，")
		elif x == 6:
			original_board("街頭+對話框.png")
		elif x == 7:
			show_text_1("不過也不確定自己是不是真的想和沒那麼熟的人出去。")
		elif x == 8:
			original_board("街頭+對話框.png")
		elif x == 9:
			show_text_1("該念的書還是得念吧，都進這間學校了......")
		elif x == 10:
			change_background("街頭+對話框.png", "宿舍+對話框.png", 30)
			x += 1
		elif x == 11:
			original_board("宿舍+對話框.png")
		elif x == 12:
			show_text_1("(放下會計課本休息一下...)")
		elif x == 13:
			original_board("宿舍+對話框.png")
		elif x == 14:
			show_text_1("不知道智則今天去哪玩了呢？")
		elif x == 15:
			original_board("宿舍+對話框.png")
			x += 1
		elif x == 16:
			show_text_1("開學到現在，其實並不排斥這科系要學的科目，")
		elif x == 17:
			show_text_2("但也不確定是不是真的喜歡。")
		elif x == 18:
			show_text_3("大概也是得走過才知道路有多崎嶇，")
		elif x == 19:
			show_text_4("還是別抱怨了吧。")
		elif x == 20:
			original_board("宿舍+對話框.png")
		elif x == 21:
			show_text_1("好了，下一科。")
		elif x == 22:
			change_background("宿舍+對話框.png", "黒+對話框.png", 30)
			x += 1
		elif x == 23:
			original_board("黒+對話框.png")
		elif x == 24:
			show_text_1("線性代數好難啊。")
		elif x == 25:
			original_board("黒+對話框.png")
		elif x == 26:
			show_text_1("進行投影")
			show_text_2("是因為不是每個問題都有解答")
		elif x == 27:
			original_board("黒+對話框.png")
		elif x == 28:
			show_text_1("限制式多")
			show_text_2("而能控制的變數太少")
			show_text_3("就像想用單一的顏色畫出這座城市")
		elif x == 29:
			original_board("黒+對話框.png")
		elif x == 30:
			show_text_1("或許我們所有人或多或少都不屬於這個空間")
		elif x == 31:
			show_text_2("而我們還是努力地在這個世界")
		elif x == 32:
			show_text_3("尋求那個屬於我們的最佳投影。")
		elif x == 33:
			change_background("黒+對話框.png", "第二章.png", 30)
			par += 1
			x = 0
			
	elif par == 20:
		choice = 0
		x = 0
		goch1 = False	

		


def chapter_2():
	global x, goch2, par, theblock_for_changing_background, playmusic1_2, playmusic2, nowplaying, musicfrom, choice, z, playmusic3
	
	if par == 0:
		original_board("第二章.png")
		pygame.time.delay(1500)
		original_board("第二章.png")
		change_background("第二章.png", "校園+對話框.png", 30)
		par += 1
	
	if par == 1:
		theblock_for_changing_background = 12 + 1
		
		if playmusic2 == True:
			pygame.mixer.music.fadeout(1000)
			pygame.mixer.music.load("timetolove_october.mp3")
			musicfrom = 0
			nowplaying = "timetolove_october.mp3"
			pygame.mixer.music.play(-1)	
			playmusic2 = False
			
		
		if x == 0:
			original_board("校園+對話框.png")
			x += 1
		elif x == 1:
			show_text_1("中秋節快到了，最近校園中充滿著對連假的期待。")
		elif x == 2:
			show_text_2("人們嘴裡談論的不是連假要去哪裡玩，就是要去哪裡烤肉。")
		elif x == 3:
			show_text_3("對於負笈求學的遊子來說，也是難得能回家一次的機會。")
		elif x == 4:
			original_board("校園+對話框.png")
			x += 1
		elif x == 5:
			show_text_1("我應該要回家嗎……")
		elif x == 6:
			original_board("校園+對話框.png")
			x += 1
		elif x == 7:
			show_text_1("老實說並沒有特別想家。")
		elif x == 8:
			show_text_2("爸媽偶爾會傳來關心的訊息，問問天氣變冷沒、生活適不適應之類，")
		elif x == 9:
			show_text_3("也有問我連假會不會回去，又說如果功課忙沒空回去沒關係。")
		elif x == 10:
			original_board("校園+對話框.png")
			x += 1
		elif x == 11:
			show_text_1("但聽起來是希望我回去的。")
		elif x == 12:
			change_background("校園+對話框.png", "校園+好朋友+對話框+名字框.png", 30)
			par += 1
			x = 0
			
	elif par == 2:
		theblock_for_changing_background = 7 + 1
		if x == 0:
			original_board("校園+好朋友+對話框+名字框.png")
			x += 1
		elif x == 1:
			show_text_name_for_4("神谷   智則")
			show_text_1("中秋連假有什麼計畫嗎？要不要來…")
		elif x == 2:
			show_text_2("對了，你不是本地人吧？你會回家嗎？")
		elif x == 3:
			original_board("校園+好朋友+對話框+名字框.png")
			x += 1
		elif x == 4:
			show_text_name_for_4("御影   翔平˙")
			show_text_1("我……")
		elif x == 5:
			original_board("校園+好朋友+對話框+名字框.png")
			x += 1
		elif x == 6:
			button_for_chapter("會回家",100, 580, 800, 30, 2, dark_gray, black, whattodo = "會回家")
			button_for_chapter("不回家", 100, 620, 800, 30, 2, dark_gray, black, whattodo = "不回家")
		if x > 6:
			x = 6
		if z == 1:
			change_background("校園+好朋友+對話框+名字框.png", "校園+好朋友+對話框+名字框.png", 30)
			par += 1
			x = 0

	elif par == 3 and choice == 1:
		z = 0
		theblock_for_changing_background = 9 + 1
		if x == 0:
			original_board("校園+好朋友+對話框+名字框.png")
			x += 1			
		elif x == 1:
			show_text_name_for_4("神谷   智則")
			show_text_1("自己離家求學應該很辛苦吧，")
		elif x == 2:
			show_text_2("不過像我這種人就會抱怨離家太近了，哈哈！")
		elif x == 3:
			original_board("校園+好朋友+對話框+名字框.png")
			x += 1
		elif x == 4:
			show_text_name_for_4("御影   翔平˙")
			show_text_1("人總是會對現狀抱怨吧，哈哈！")
		elif x == 5:
			original_board("校園+好朋友+對話框+名字框.png")
			x += 1
		elif x == 6:
			show_text_name_for_4("神谷   智則")
			show_text_1("不過家人是很重要的呢，連假結束見啦，中秋節快樂！")
		elif x == 7:
			original_board("校園+好朋友+對話框+名字框.png")
			x += 1
		elif x == 8:
			show_text_name_for_4("御影   翔平˙")
			show_text_1("中秋節快樂~")
		elif x == 9:
			change_background("校園+好朋友+對話框+名字框.png", "宿舍+對話框.png", 30)
			par += 1
			x = 0
			
	elif par == 4 and choice == 1:
		theblock_for_changing_background = 6 + 1
		if x == 0:
			original_board("宿舍+對話框.png")
			x += 1			
		elif x == 1:
			show_text_1("沒事先訂票的話，要回家就得坐一趟貴到哭的高鐵，")
		elif x == 2:
			show_text_2("或者便宜一點但要花四到五小時的火車。")
		elif x == 3:
			original_board("宿舍+對話框.png")
			x += 1			
		elif x == 4:
			show_text_1("爸媽雖然說不要擔心錢的問題，")
		elif x == 5:
			show_text_2("但在外面生活才知道處處都要花錢的感覺。")
		elif x == 6:
			change_background("宿舍+對話框.png", "夜景+對話框.png", 30)
			par += 1
			x = 0
			
	elif par == 5 and choice == 1:
		theblock_for_changing_background = 8 + 1
		if x == 0:
			original_board("夜景+對話框.png")
			x += 1
		elif x == 1:
			show_text_1("於是跟著車站的人山人海漂流回到家鄉。")
		elif x == 2:
			show_text_2("日暮向晚時分，南方的空氣飄著幾分溫暖和人情。")
		elif x == 3:
			show_text_3("回到熟悉的地方，感覺總是好的。")
		elif x == 4:
			original_board("夜景+對話框.png")
			x += 1
		elif x == 5:
			show_text_1("一個多月沒有關心家裡的消息，越靠近家門越感到有點卻步。")
		elif x == 6:
			original_board("夜景+對話框.png")
			x += 1
		elif x == 7:
			show_text_1("家裡的慣例是中秋吃火鍋，我們圍著餐桌，一切就像我沒出門過。")
		elif x == 8:
			change_background("夜景+對話框.png", "烤肉1+對話框+名字框.png", 30)
			par += 1
			x = 0
			
	elif par == 6 and choice == 1:
		theblock_for_changing_background = 15 + 1
		if x == 0:
			original_board("烤肉1+對話框+名字框.png")
			x += 1
		elif x == 1:
			show_text_name_for_4("翔平   他爸")
			show_text_1("生活還習慣吧？課業順利嗎^^")
		elif x == 2:
			original_board("烤肉1+對話框+名字框.png")
			x += 1
		elif x == 3:
			show_text_name_for_4("御影   翔平")
			show_text_1("乾你屁事^^")
		elif x == 4:
			original_board("烤肉1+對話框+名字框.png")
			x += 1
		elif x == 5:
			show_text_1("我們用著熟悉的模式對談，沒有什麼比這更讓人感到溫暖的了。")
		elif x == 6:
			original_board("烤肉1+對話框+名字框.png")
			x += 1
		elif x == 7:
			show_text_1("明月下沉，隱約的也想記著這頓飯的滋味，帶回學校去。")
		elif x == 8:
			original_board("烤肉1+對話框+名字框.png")
			x += 1
		elif x == 9:
			show_text_1("(臨走前)")
		elif x == 10:
			original_board("烤肉1+對話框+名字框.png")
			x += 1
		elif x == 11:
			show_text_name_for_4("翔平   媽")
			show_text_1("下次回來什麼時候啊？")
		elif x == 12:
			original_board("烤肉1+對話框+名字框.png")
			x += 1
		elif x == 13:
			show_text_name_for_4("御影   翔平")
			show_text_1("乾你…")
		elif x == 14:
			show_text_2("…沒有啦，有空會盡量回來的。")
		elif x == 15:
			change_background("烤肉1+對話框+名字框.png", "第三章.png", 30)
			x = 0
			choice = 0
			goch2 = False
			
	elif par == 3 and choice == 2:
		z = 0
		theblock_for_changing_background = 18 + 1
		if x == 0:
			original_board("校園+好朋友+對話框+名字框.png")
			x += 1
		elif x == 1:
			show_text_name_for_4("神谷   智則")
			show_text_1("喔？那要不要來我家？")
		elif x == 2:
			show_text_2("我家每年這時候都會烤肉，我爸每年也都叫我找朋友來。")
		elif x == 3:
			show_text_3("怎麼樣，可以溫暖你的胃跟你的心喔，河河河河河——")
		elif x == 4:
			original_board("校園+好朋友+對話框+名字框.png")
			x += 1
		elif x == 5:
			show_text_name_for_4("御影   翔平")
			show_text_1("這樣啊…好像挺划算的喔？")
		elif x == 6:
			original_board("校園+好朋友+對話框+名字框.png")
			x += 1
		elif x == 7:
			show_text_name_for_4("神谷   智則")
			show_text_1("該來烤肉了吧！")
		elif x == 8:
			original_board("校園+好朋友+對話框+名字框.png")
			x += 1
		elif x == 9:
			show_text_name_for_4("御影   翔平")
			show_text_1("該烤肉了嗎？")
		elif x == 10:
			original_board("校園+好朋友+對話框+名字框.png")
			x += 1
		elif x == 11:
			show_text_name_for_4("神谷   智則")
			show_text_1("是時候烤肉了！")
		elif x == 12:
			original_board("校園+好朋友+對話框+名字框.png")
			x += 1
		elif x == 13:
			show_text_name_for_4("御影   翔平")
			show_text_1("要烤肉就趁這時候了！")
		elif x == 14:
			original_board("校園+好朋友+對話框+名字框.png")
			x += 1
		elif x == 15:
			show_text_name_for_4("神谷   智則")
			show_text_1("那就到時候見吧！")
		elif x == 16:
			original_board("校園+好朋友+對話框+名字框.png")
			x += 1
		elif x == 17:
			show_text_name_for_4("御影   翔平")
			show_text_1("也只能到時候見了！")
		elif x == 18:
			change_background("校園+好朋友+對話框+名字框.png", "烤肉1+對話框+名字框.png", 30)
			par += 1
			x = 0
	
	elif par == 4 and choice == 2:
		theblock_for_changing_background = 16 + 1
		if x == 0:
			original_board("烤肉1+對話框+名字框.png")
			x += 1
		elif x == 1:
			show_text_1("(中秋當晚)")
		elif x == 2:
			original_board("烤肉1+對話框+名字框.png")
			x += 1
		elif x == 3:
			show_text_1("智則家聚集了很多人，")
		elif x == 4:
			show_text_2("智則說每年他們家都廣邀親朋好友和街坊鄰居。")
		elif x == 5:
			show_text_3("不管認不認識，來到這裡就是他們的一份子。")
		elif x == 6:
			original_board("烤肉1+對話框+名字框.png")
			x += 1
		elif x == 7:
			show_text_name_for_4("御影   翔平")
			show_text_1("叔叔阿姨好~")
		elif x == 8:
			original_board("烤肉1+對話框+名字框.png")
			x += 1
		elif x == 9:
			show_text_name_for_4("智則   他媽")
			show_text_1("多吃一點啊，不要回家的時候還買泡麵回去吃喔，哈哈！")
		elif x == 10:
			original_board("烤肉1+對話框+名字框.png")
			x += 1
		elif x == 11:
			show_text_name_for_4("智則   他爸")
			show_text_1("吃完三盤才能走啊，沒在跟你廢話")
		elif x == 12:
			original_board("烤肉1+對話框+名字框.png")
			x += 1
		elif x == 13:
			show_text_1("附近就是海邊，在外面邊吹風邊烤肉相當舒服。")
		elif x == 14:
			show_text_2("大人們有的忙著張羅食物，有的圍著圈泡茶聊天，")
		elif x == 15:
			show_text_3("圍繞著大家的則是追逐打鬧的小朋友們。")
		elif x == 16:
			change_background("烤肉1+對話框+名字框.png", "烤肉1+好朋友+對話框+名字框.png", 30)
			par += 1
			x = 0
			
	elif par == 5 and choice == 2:
		theblock_for_changing_background = 19 + 1
		if x == 0:
			original_board("烤肉1+好朋友+對話框+名字框.png")
			x += 1
		elif x == 1:
			show_text_name_for_4("神谷   智則")
			show_text_1("玩的開心嗎？")
		elif x == 2:
			original_board("烤肉1+好朋友+對話框+名字框.png")
			x += 1
		elif x == 3:
			show_text_name_for_4("御影   翔平")
			show_text_1("滿好玩的啊，我喜歡這裡的氛圍。")
		elif x == 4:
			show_text_2("你爸媽人也都好好，每年都辦這種活動，讓平常不常見的人們能聚在一起。")
		elif x == 5:
			original_board("烤肉1+好朋友+對話框+名字框.png")
			x += 1
		elif x == 6:
			show_text_name_for_4("神谷   智則")
			show_text_1("哈哈，他們只是比較愛熱鬧啦。")
		elif x == 7:
			original_board("烤肉1+好朋友+對話框+名字框.png")
			x += 1
		elif x == 8:
			show_text_name_for_4("御影   翔平")
			show_text_1("真羨慕啊，我也想在這種環境下長大。")
		elif x == 9:
			original_board("烤肉1+好朋友+對話框+名字框.png")
			x += 1
		elif x == 10:
			show_text_name_for_4("神谷   智則")
			show_text_1("那怎麼樣，有溫暖到你的心嗎？(微笑)")
		elif x == 11:
			original_board("烤肉1+好朋友+對話框+名字框.png")
			x += 1
		elif x == 12:
			show_text_name_for_4("御影   翔平")
			show_text_1("什麼…難道你…(心跳)")
		elif x == 13:
			original_board("烤肉1+好朋友+對話框+名字框.png")
			x += 1
		elif x == 14:
			show_text_name_for_4("神谷   智則")
			show_text_1("沒有錯…")
		elif x == 15:
			original_board("烤肉1+好朋友+對話框+名字框.png")
			x += 1
		elif x == 16:
			show_text_name_for_4("御影   翔平")
			show_text_1("可是智則，我…")
		elif x == 17:
			show_text_2("我…")
		elif x == 18:
			show_text_3("我…")
		elif x == 19:
			original_board("烤肉1+好朋友+對話框+名字框.png")
			x += 1
		elif x == 20:
			button_for_chapter("我需要治療！", 100, 580, 800, 30, 2, dark_gray, black, whattodo = "我需要治療！")
			button_for_chapter("我需要治療！", 100, 620, 800, 30, 2, dark_gray, black, whattodo = "我需要治療！")
			button_for_chapter("我需要治療！", 100, 660, 800, 30, 2, dark_gray, black, whattodo = "我需要治療！")
		if x > 20:
			x = 20
		if z == 1:
			change_background("烤肉1+好朋友+對話框+名字框.png", "烤肉1+好朋友和女主+對話框+名字框.png", 30)
			par += 1
			x = 0
			
	elif par == 6 and choice == 2:
		z = 0
		theblock_for_changing_background = 8 + 1
		if x == 0:
			original_board("烤肉1+好朋友和女主+對話框+名字框.png")
			x += 1
		elif x == 1:
			show_text_name_for_4("榊原   凜")
			show_text_1("你們在幹嘛？")
		elif x == 2:
			original_board("烤肉1+好朋友和女主+對話框+名字框.png")
			x += 1
		elif x == 3:
			show_text_name_for_4("御影   翔平")
			show_text_1("嗨阿凜，原來妳也來了")
		elif x == 4:
			original_board("烤肉1+好朋友和女主+對話框+名字框.png")
			x += 1
		elif x == 5:
			show_text_name_for_4("榊原   凜")
			show_text_1("我從認識智則後每年都來吃啊")
		elif x == 6:
			original_board("烤肉1+好朋友和女主+對話框+名字框.png")
			x += 1
		elif x == 7:
			show_text_name_for_4("神谷   智則")
			show_text_1("也吃得差不多了，我們出去走走吧。")
		elif x == 8:
			change_background("烤肉1+好朋友和女主+對話框+名字框.png", "夜景+好朋友和女主+對話框+名字框.png", 30)
			par += 1
			x = 0
			
	elif par == 7 and choice == 2:
		theblock_for_changing_background = 27 + 1
		if x == 0:
			original_board("夜景+好朋友和女主+對話框+名字框.png")
			x += 1
		elif x == 1:
			show_text_name_for_4("榊原   凜")
			show_text_1("哈啊，吃得好飽！對了翔平你沒回家啊？")
		elif x == 2:
			original_board("夜景+好朋友和女主+對話框+名字框.png")
			x += 1
		elif x == 3:
			show_text_name_for_4("御影   翔平")
			show_text_1("也才剛開學沒多久，就沒特別想回去了。")
		elif x == 4:
			original_board("夜景+好朋友和女主+對話框+名字框.png")
			x += 1
		elif x == 5:
			show_text_name_for_4("榊原   凜")
			show_text_1("這樣喔，離家求學很辛苦吧！")
		elif x == 6:
			show_text_2("上大學之後才發現大學生活跟想像的差很多呢。")
		elif x == 7:
			original_board("夜景+好朋友和女主+對話框+名字框.png")
			x += 1
		elif x == 8:
			show_text_name_for_4("御影   翔平")
			show_text_1("下禮拜小考你們唸了嗎？")
		elif x == 9:
			original_board("夜景+好朋友和女主+對話框+名字框.png")
			x += 1
		elif x == 10:
			show_text_name_for_4("神谷   智則")
			show_text_1("下禮拜有小考？")
		elif x == 11:
			original_board("夜景+好朋友和女主+對話框+名字框.png")
			x += 1
		elif x == 12:
			show_text_name_for_4("榊原   凜")
			show_text_1("太廢了吧，你到底怎麼考進來的啊？")
		elif x == 13:
			original_board("夜景+好朋友和女主+對話框+名字框.png")
			x += 1
		elif x == 14:
			show_text_name_for_4("神谷   智則")
			show_text_1("「我乃指考榜首。」")
		elif x == 15:
			original_board("夜景+好朋友和女主+對話框+名字框.png")
			x += 1
		elif x == 16:
			show_text_name_for_4("榊原   凜")
			show_text_1("「你指考榜首？我乃女主角。」")
		elif x == 17:
			original_board("夜景+好朋友和女主+對話框+名字框.png")
			x += 1
		elif x == 18:
			show_text_name_for_4("御影   翔平")
			show_text_1("「你好，女主角。我乃主角，久仰久仰。」")
		elif x == 19:
			original_board("夜景+好朋友和女主+對話框+名字框.png")
			x += 1
		elif x == 20:
			show_text_name_for_4("榊原   凜")
			show_text_1("你也懂此梗？")
		elif x == 21:
			original_board("夜景+好朋友和女主+對話框+名字框.png")
			x += 1
		elif x == 22:
			show_text_name_for_4("御影   翔平")
			show_text_1("我有想好幾組可以講。此小考使我苦惱，我只好果敢點，考好考滿。")
		elif x == 23:
			original_board("夜景+好朋友和女主+對話框+名字框.png")
			x += 1
		elif x == 24:
			show_text_name_for_4("神谷   智則")
			show_text_1("可以。")
		elif x == 25:
			original_board("夜景+好朋友和女主+對話框+名字框.png")
			x += 1
		elif x == 26:
			show_text_name_for_4("榊原   凜")
			show_text_1("你頗屌。")
		elif x == 27:
			change_background("夜景+好朋友和女主+對話框+名字框.png", "烤肉1+好朋友和女主+對話框+名字框.png", 30)
			par += 1
			x = 0
			
	elif par == 8 and choice == 2:
		theblock_for_changing_background = 13 + 1
		if x == 0:
			original_board("烤肉1+好朋友和女主+對話框+名字框.png")
			x += 1
		elif x == 1:
			show_text_1("走著走著，時間也有點晚了。")
		elif x == 2:
			show_text_2("和智則的家人道別後，我想我必須要離開")
		elif x == 3:
			show_text_3("了。")
		elif x == 4:
			original_board("烤肉1+好朋友和女主+對話框+名字框.png")
			x += 1
		elif x == 5:
			show_text_name_for_4("榊原   凜")
			show_text_1("謝謝你找我來，我玩得很開心")
		elif x == 6:
			original_board("烤肉1+好朋友和女主+對話框+名字框.png")
			x += 1
		elif x == 7:
			show_text_name_for_4("神谷   智則")
			show_text_1("哈哈，感謝來玩，你果然是很有趣的人啊！")
		elif x == 8:
			original_board("烤肉1+好朋友和女主+對話框+名字框.png")
			x += 1
		elif x == 9:
			show_text_name_for_4("榊原   凜")
			show_text_1("對啊，本來還覺得你好像有點陰沉，但你屁話其實不少啊xD 掰啦~")
		elif x == 10:
			original_board("烤肉1+好朋友和女主+對話框+名字框.png")
			x += 1
		elif x == 11:
			show_text_1("滿月的夜晚，心中似乎改變了什麼，")
		elif x == 12:
			show_text_2("不過隱約覺得是踏實的，感覺還不錯。")
		elif x == 13:
			change_background("烤肉1+好朋友和女主+對話框+名字框.png", "第三章.png", 30)
			x = 0
			choice = 0
			goch2 = False



			
def chapter_3():
	global x, goch3, par, theblock_for_changing_background, playmusic2, playmusic3, playmusic4, nowplaying, musicfrom, choice, z
	
	if par == 0:
		original_board("第三章.png")
		pygame.time.delay(1500)
		original_board("第三章.png")
		change_background("第三章.png", "小街+對話框.png", 30)
		par += 1
	
	if par == 1:
		theblock_for_changing_background = 8 + 1
		
		if playmusic3 == True:
			pygame.mixer.music.fadeout(1000)
			pygame.mixer.music.load("kara_m01.mp3")
			musicfrom = 0
			nowplaying = "kara_m01.mp3"
			pygame.mixer.music.play(-1)	
			playmusic3 = False
		
		if x == 0:
			original_board("小街+對話框.png")
		elif x == 1:
			show_text_1("這天吃完早餐準備去上課，")
		elif x == 2:
			show_text_2("走著走著，發現前方路上有張學生證。")
		elif x == 3:
			original_board("小街+對話框.png")
			x += 1
		elif x == 4:
			show_text_1("B0X70XXXX，XXX，照片是個男生，從學號看應該和我一樣是管院的人。")
		elif x == 5:
			original_board("小街+對話框.png")
			x += 1
		elif x == 6:
			show_text_1("這個嘛…我應該要…")
		elif x == 7:#button
			original_board("小街+對話框.png")
			x += 1
		elif x == 8:
			button_for_chapter("物歸原位(丟回去)",100, 580, 800, 30, 2, dark_gray, black, whattodo = "物歸原位(丟回去)")
			button_for_chapter("先收著", 100, 620, 800, 30, 2, dark_gray, black, whattodo = "先收著")
			button_for_chapter("PO學校交流板", 100, 660, 800, 30, 2, dark_gray, black, whattodo = "PO學校交流板")
		if x > 8:
			x = 8
		if z == 1:
			change_background("小街+對話框.png", "小街+對話框.png", 30)
			par += 1
			x = 0
			
	elif par == 2:
		theblock_for_changing_background = 3 + 1
		z = 0
		if x == 1:
			original_board("小街+對話框.png")
			x += 1
		elif x == 2:
			show_text_1("總之先進教室吧。")			
		elif x == 3:
			change_background("小街+對話框.png", "教室+對話框.png", 30)
			par += 1
			x = 0
			
	elif par == 3:
		theblock_for_changing_background = 2 + 1
		if x == 0:
			original_board("教室+對話框.png")
		elif x == 1:
			show_text_1("課上到一半，有人拍了拍我的肩膀")
		elif x == 2:
			change_background("教室+對話框.png", "教室+女主+對話框+名字框.png", 30)
			par += 1
			x = 0
	
	
	elif par == 4:
		theblock_for_changing_background = 30 + 1
		if x == 0:
			original_board("教室+女主+對話框+名字框.png")
			x += 2
		elif x == 2:
			show_text_name_for_4("榊原   凜")
			show_text_1("這裡有人坐嗎？")
		elif x == 3:
			original_board("教室+女主+對話框+名字框.png")
			x += 1
		elif x == 4:
			show_text_1("凜突然從我後面出現，挑了我旁邊的位置坐下來。")
		elif x == 5:
			original_board("教室+女主+對話框+名字框.png")
			x += 1
		elif x == 6:
			show_text_name_for_4("御影   翔平")
			show_text_1("怎樣，睡過頭喔？")
		elif x == 7:
			original_board("教室+女主+對話框+名字框.png")
			x += 1
		elif x == 8:
			show_text_name_for_4("榊原   凜")
			show_text_1("對啊，昨天就念書念滿晚的。")
		elif x == 9:
			original_board("教室+女主+對話框+名字框.png")
			x += 1
		elif x == 10:
			show_text_name_for_4("榊原   凜")
			show_text_1("上次小考不太好考啊，平均分數竟然不及格，這教授聽說每年都當很多人耶。")
		elif x == 11:
			show_text_2("你上次考多少啊？")
		elif x == 12:
			original_board("教室+女主+對話框+名字框.png")
			x += 1
		elif x == 13:
			show_text_name_for_4("御影   翔平")
			show_text_1("65")
		elif x == 14:
			original_board("教室+女主+對話框+名字框.png")
			x += 1
		elif x == 15:
			show_text_name_for_4("榊原   凜")
			show_text_1("哈，我高你一點，68。不過這樣下去期末有點危險呢。")
		elif x == 16:
			original_board("教室+女主+對話框+名字框.png")
			x += 1
		elif x == 17:
			show_text_name_for_4("御影   翔平")
			show_text_1("我也覺得，大概是得再努力一點才行。就業率100%的學校，還是沒那麼輕鬆吧。")
		elif x == 18:
			original_board("教室+女主+對話框+名字框.png")
			x += 1
		elif x == 19:
			show_text_name_for_4("榊原   凜")
			show_text_1("還是我們來比期末考的分數，輸的請吃飯，怎麼樣？")
		elif x == 20:
			original_board("教室+女主+對話框+名字框.png")
			x += 1
		elif x == 21:
			show_text_name_for_4("御影   翔平")
			show_text_1("可以啊，講得好像妳會贏一樣")
		elif x == 22:
			original_board("教室+女主+對話框+名字框.png")
			x += 1
		elif x == 23:
			show_text_name_for_4("榊原   凜")
			show_text_1("也不想想這次是誰贏了喔，你是不是該先請我點什麼啊？")
		elif x == 24:
			original_board("教室+女主+對話框+名字框.png")
			x += 1
		elif x == 25:
			show_text_name_for_4("御影   翔平")
			show_text_1("請妳什麼？")
		elif x == 26:
			original_board("教室+女主+對話框+名字框.png")
			x += 1
		elif x == 27:
			show_text_name_for_4("榊原   凜")
			show_text_1("我口有點渴，你可以請我冷飲。")
		elif x == 28:
			original_board("教室+女主+對話框+名字框.png")
			x += 1
		elif x == 29:
			show_text_name_for_4("御影   翔平")
			show_text_1("請你老母。")
		elif x == 30:
			change_background("教室+女主+對話框+名字框.png", "教室+對話框.png", 30)
			par += 1
			x = 0
			
			
	elif par == 5:
		theblock_for_changing_background = 2 + 1
		if x == 0:
			original_board("教室+對話框.png")
			x += 1
		elif x == 1:
			show_text_1("(下課鐘聲響起)")
		elif x == 2: #1:ch3結束  2:par +=1 3:par += 3
			if choice == 1:
				change_background("教室+對話框.png", "第四章.png", 30)
				par = 9
				x = 0
			elif choice == 2:
				change_background("教室+對話框.png", "教室+對話框.png", 30)
				par += 1
				x = 0
				choice = 0
			elif choice == 3:
				change_background("教室+對話框.png", "教室+對話框.png", 30)
				par += 3
				x = 0
				choice = 0
			
			
	elif par == 6:
		theblock_for_changing_background = 4 + 1
		if x == 0:
			original_board("教室+對話框.png")
			x += 1
		elif x == 1:
			show_text_1("我拿出學生證開始研究。")
		elif x == 2:
			original_board("教室+對話框.png")
			x += 1
		elif x == 3:
			show_text_1("照片中的男生理著平頭，皮膚偏蒼白，臉有點消瘦，眼窩有點凹陷。")
		elif x == 4:
			change_background("教室+對話框.png", "教室+女主+對話框+名字框.png", 30)
			par += 1
			x = 0
			
			
	elif par == 7:
		theblock_for_changing_background = 12 + 1
		if x == 0:
			original_board("教室+女主+對話框+名字框.png")
			x += 1
		elif x == 1:
			show_text_name_for_4("榊原   凜")
			show_text_1("欸？這是我朋友的學生證，怎麼在你這？")
		elif x == 2:
			original_board("教室+女主+對話框+名字框.png")
			x += 1
		elif x == 3:
			show_text_name_for_4("御影   翔平")
			show_text_1("這個喔，就路上撿到的，你認識他嗎？")
		elif x == 4:
			original_board("教室+女主+對話框+名字框.png")
			x += 1
		elif x == 5:
			show_text_name_for_4("榊原   凜")
			show_text_1("對啊，社團認識的朋友。")
		elif x == 6:
			original_board("教室+女主+對話框+名字框.png")
			x += 1
		elif x == 7:
			show_text_name_for_4("御影   翔平")
			show_text_1("是喔，那他有在吸毒嗎？")
		elif x == 8:
			original_board("教室+女主+對話框+名字框.png")
			x += 1
		elif x == 9:
			show_text_name_for_4("榊原   凜")
			show_text_1("哈哈哈哈他很可憐，長得超像吸毒犯，下次去問他是不是在吸XD 幫你還他嗎？")
		elif x == 10:
			original_board("教室+女主+對話框+名字框.png")
			x += 1
		elif x == 11:
			show_text_name_for_4("御影   翔平")
			show_text_1("主角：哈哈好的，交給妳了。")
		elif x == 12:
			change_background("教室+女主+對話框+名字框.png", "第四章.png", 30)
			par = 9
			x = 0

	elif par == 8:
		theblock_for_changing_background = 19 + 1
		if x == 0:
			original_board("教室+對話框.png")
			x += 1
		elif x == 1:
			show_text_1("下課後我把學生證的照片放到交流版。")
		elif x == 2:
			original_board("教室+對話框.png")
			x += 1
		elif x == 3:
			show_text_1("「XX系XXX，請認識的人幫忙tag他。」")
		elif x == 4:
			original_board("教室+對話框.png")
			x += 1
		elif x == 5:
			show_text_1("底下的留言紛紛串聯起來。")
		elif x == 6:
			original_board("教室+對話框.png")
			x += 1
		elif x == 7:
			show_text_1("「欸你的學生證啦」")
		elif x == 8:
			show_text_2("「怎麼又掉了啊？」")
		elif x == 9:
			show_text_3("「笑死，是不是差點補發第10次啊」")
		elif x == 10:
			original_board("教室+對話框.png")
			x += 1
		elif x == 11:
			show_text_1("不久後那個人就來找我。")
		elif x == 12:
			original_board("教室+對話框.png")
			x += 1
		elif x == 13:
			show_text_1("拿回了學生證，他的眼裡滿是感激。")
		elif x == 14:
			original_board("教室+對話框.png")
			x += 1
		elif x == 15:
			show_text_1("有時候幫助人最棒的回報就是看到這種表情吧，")
		elif x == 16:
			original_board("教室+對話框.png")
			x += 1
		elif x == 17:
			show_text_1("那是失而復得的喜悅。")
		elif x == 18:
			change_background("教室+對話框.png", "第四章.png", 30)
			par = 9
			x = 0
			
	elif par == 9:
		choice = 0
		par += 1
		x = 0
		goch3 = False


def chapter_4():
	global x, goch4, par, theblock_for_changing_background, playmusic1,playmusic1_2, playmusic2, playmusic3, playmusic4, play_ed, nowplaying, musicfrom, choice, z
	
	if par == 0:
		original_board("第四章.png")
		pygame.time.delay(1500)
		original_board("第四章.png")
		change_background("第四章.png", "運動場+好朋友+對話框+名字框.png", 30)
		par += 1

	if par == 1:
		theblock_for_changing_background = 11 + 1
		if x == 0:
			original_board("運動場+好朋友+對話框+名字框.png")
		elif x == 1:
			show_text_name_for_4("神谷   智則")
			show_text_1("欸欸翔平，要不要報名網球比賽啊？")
		elif x == 2:
			show_text_3("智則手中拿著一張傳單。")
		elif x == 3:
			original_board("運動場+好朋友+對話框+名字框.png")
			x += 1
		elif x == 4:
			show_text_name_for_4("御影   翔平")
			show_text_1("比賽？誰辦的啊？")
		elif x == 5:
			show_text_2("可是我不會打網球耶")
		elif x == 6:
			original_board("運動場+好朋友+對話框+名字框.png")
			x += 1
		elif x == 7:
			show_text_name_for_4("神谷   智則")
			show_text_1("好像是系上辦的吧。很簡單的啦你一定會，按幾個按鍵就能打了")
		elif x == 8:
			show_text_2("打贏了還有獎金可以拿喔!")
		elif x == 9:
			original_board("運動場+好朋友+對話框+名字框.png")
			x += 1
		elif x == 10:
			show_text_name_for_4("御影   翔平")
		elif x == 11:
			button_for_chapter("參加",100, 580, 800, 30, 2, dark_gray, black, whattodo = "參加")
			button_for_chapter("要不要參加呢.....參加好了", 100, 620, 800, 30, 2, dark_gray, black, whattodo = "參加")
			button_for_chapter("恩...不要參加好了...不過是智則他邀請我的欸...恩..還是參加好了", 100, 660, 800, 30, 2, dark_gray, black, whattodo = "參加")
		if x > 11:
			x = 11
		if z == 1:
			change_background("運動場+好朋友+對話框+名字框.png", "教室+對話框+名字框.png", 15)
			par += 1
			x = 0
			z = 0
			goch4 = False
			

def chapter_8():
	global x, goch8, par, theblock_for_changing_background, playmusic1,playmusic1_2, playmusic2, playmusic3, playmusic4, play_ed, nowplaying, musicfrom, choice, z, fade_out
	
	if par == 0:
		original_board("第八章.png")
		pygame.time.delay(1500)
		original_board("第八章.png")
		change_background("第八章.png", "夜景+對話框.png", 30)
		par += 1
	
	if par == 1:
		theblock_for_changing_background = 13 + 1
		if x == 0:
			original_board("夜景+對話框.png")
		elif x == 1:
			show_text_1("日子來到十二月")
		elif x == 2:
			show_text_2("出門必須加件厚外套，陽光偶爾露臉的季節")
		elif x == 3:
			original_board("夜景+對話框.png")
			x += 1
		elif x == 4:
			show_text_1("街上多了幾分聖誕氣息")
		elif x == 5:
			show_text_2("人們分享著祝福，在街上比較容易看到開心的表情")
		elif x == 6:
			original_board("夜景+對話框.png")
		elif x == 7:
			show_text_1("歲末年終")
		elif x == 8:
			show_text_2("大家忙著為工作收尾，迎接新的一年")
		elif x == 9:
			original_board("夜景+對話框.png")
		elif x == 10:
			show_text_1("回顧今年，上了大學後")
			#if fade_out == True:
				#pygame.mixer.music.fadeout(1000)
				#fade_out = False
		elif x == 11:
			show_text_2("我是否有些變化了？")
		elif x == 12:
			show_text_3("這些變化是好事嗎？")
		elif x == 13:
			change_background("夜景+對話框.png", "教室+對話框+名字框.png", 15)
			par += 1
			x = 0
			
	elif par == 2:
		theblock_for_changing_background = 3 + 1
		if x == 0:
			original_board("教室+對話框+名字框.png")
		elif x == 1:
			show_text_name_for_2("教授")
			show_text_1("同學們，好好準備期末考啊。")
		elif x == 2:
			show_text_2("成績是你自己的，教授沒辦法幫你負責啊~")
		elif x == 3:
			change_background("教室+對話框+名字框.png", "黒+對話框.png", 15)
			par += 1
			x = 0
			
	elif par == 3:
		theblock_for_changing_background = 5 + 1
		if x == 0:
			original_board("黒+對話框.png")
		elif x == 1:
			show_text_1("聖誕節大家會怎麼過呢？")
		elif x == 2:
			original_board("黒+對話框.png")
		elif x == 3:
			show_text_1("智則大概會好好享受這節日吧")
		elif x == 4:
			show_text_2("說不定他家又要辦個什麼派對了")
		elif x == 5:
			change_background("黒+對話框.png", "黒+女主+對話框.png", 30)
			par += 1
			x = 0
	
	elif par == 4:
		theblock_for_changing_background = 4 + 1
		if x == 0:
			original_board("黒+女主+對話框.png")
		elif x == 1:
			show_text_1("那凜呢？")
		elif x == 2:
			show_text_2("凜會出去慶祝嗎？")
		elif x == 3:
			show_text_3("或是在家準備考試？")
		elif x == 4:
			change_background("黒+女主+對話框.png", "黒+對話框.png", 30)
			par += 1
			x = 0
			
	elif par == 5:
		theblock_for_changing_background = 26 + 1
		if x == 0:
			original_board("黒+對話框.png")
		elif x == 1:
			show_text_1("我同意教授的話")
			if play_ed == True:
				pygame.mixer.music.fadeout(1000)
				ed = pygame.mixer.Sound('ed.wav')
				musicfrom = 0
				nowplaying = "ed.wav"
				ed.play(loops = 0, fade_ms = 10000)
				play_ed = False
		elif x == 2:
			show_text_2("成績是自己的，只有自己能負責")
		elif x == 3:
			original_board("黒+對話框.png")
		elif x == 4:
			show_text_1("我也曾只為此而努力")
		elif x == 5:
			original_board("黒+對話框.png")
			x += 1
		elif x == 6:
			show_text_1("成績當然重要")
		elif x == 7:
			show_text_2("不過一定有其他事物和成績相同重要")
		elif x == 8:
			show_text_3("可能沒辦法清楚的描述")
		elif x == 9:
			original_board("黒+對話框.png")
			x += 1
		elif x == 10:
			show_text_1("但在和他人相處的時候")
		elif x == 11:
			show_text_2("和朋友講幹話的時候")
		elif x == 12:
			show_text_3("圍著餐桌和家人吃飯的時候")
		elif x == 13:
			show_text_4("揮拍擊出致勝球的時候")
		elif x == 14:
			original_board("黒+對話框.png")
			x += 1
		elif x == 15:
			show_text_1("就知道我需要負責的不只是成績")
		elif x == 16:
			show_text_2("我需要負責的...")
		elif x == 17:
			show_text_3("還包含那些成就了自己的美好事物")
		elif x == 18:
			original_board("黒+對話框.png")
			x += 1
		elif x == 19:
			show_text_1("期末考結果會怎麼樣？")
		elif x == 20:
			show_text_2("我不知道")
		elif x == 21:
			original_board("黒+對話框.png")
			x += 1
		elif x == 22:
			show_text_1("那考完放寒假會怎麼樣？")
		elif x == 23:
			show_text_2("很多很多年後畢業之後會怎麼樣？")
		elif x == 24:
			original_board("黒+對話框.png")
		elif x == 25:
			show_text_1("我想答案就讓你探索吧。")
		elif x == 26:
			button_for_chapter("出發", 100, 620, 800, 30, 2, dark_gray, black, whattodo = "出發")
		if x > 26:
			x = 26
		if z == 1:
			change_background("黒+對話框.png", "blackintro.png", 30)
			par += 1
			x = 0
			goch8 = False 
		


		
def opening():
	intro_delay_time = 1500
	intro_change_speed = 48

	original_board("blackintro.png")
	change_background("blackintro.png", "sakura.jpg", 20)
	background_file = "sakura.jpg"
	original_board(background_file)
	pygame.time.delay(intro_delay_time)
	original_board(background_file)
	change_background("sakura.jpg", "aniback.jpg", intro_change_speed)

	background_file = "aniback.jpg"
	original_board(background_file)
	pygame.time.delay(intro_delay_time)
	original_board(background_file)
	change_background("aniback.jpg", "mizuumi.jpg", intro_change_speed)

	background_file = "mizuumi.jpg"
	original_board(background_file)
	pygame.time.delay(intro_delay_time)
	original_board(background_file)
	change_background("mizuumi.jpg", "clock.jpg", intro_change_speed)

	background_file = "clock.jpg"
	original_board(background_file)
	pygame.time.delay(intro_delay_time)
	original_board(background_file)
	change_background("clock.jpg", "arc.jpg", intro_change_speed)

	background_file = "arc.jpg"
	original_board(background_file)
	pygame.time.delay(intro_delay_time)
	original_board(background_file)
	change_background("arc.jpg", "校園.png", intro_change_speed)

	background_file = "校園.png"
	original_board(background_file)
	pygame.time.delay(intro_delay_time)
	original_board(background_file)
	change_background("校園.png", "blackintro.png", 40)

	background_file = "blackintro.png"
	original_board(background_file)
	change_background("blackintro.png", "start.png", 22)
		

def ending():
	global play_ed, go_ed
	
	if play_ed == True:
			pygame.mixer.music.fadeout(1000)
			ed = pygame.mixer.Sound('ed.wav')
			musicfrom = 0
			nowplaying = "ed.wav"
			ed.play(loops = 0, fade_ms = 10000)
			play_ed = False
	
	intro_delay_time = 2000
	intro_change_speed = 10

	original_board("blackintro.png")
	change_background("blackintro.png", "ed_製作委員會前.png", 20)
	
	background_file = "ed_製作委員會前.png"
	original_board(background_file)
	pygame.time.delay(intro_delay_time)
	original_board(background_file)
	change_background("ed_製作委員會前.png", "ed_製作委員會.png", intro_change_speed)

	background_file = "ed_製作委員會.png"
	original_board(background_file)
	pygame.time.delay(intro_delay_time)
	original_board(background_file)
	change_background("ed_製作委員會.png", "ed_遊戲設計.png", intro_change_speed)

	background_file = "ed_遊戲設計.png"
	original_board(background_file)
	pygame.time.delay(intro_delay_time)
	original_board(background_file)
	change_background("ed_遊戲設計.png", "ed_劇本構成.png", intro_change_speed)

	background_file = "ed_劇本構成.png"
	original_board(background_file)
	pygame.time.delay(intro_delay_time)
	original_board(background_file)
	change_background("ed_劇本構成.png", "ed_劇本協力.png", intro_change_speed)

	background_file = "ed_劇本協力.png"
	original_board(background_file)
	pygame.time.delay(intro_delay_time)
	original_board(background_file)
	change_background("ed_劇本協力.png", "ed_劇本監督.png", intro_change_speed)

	background_file = "ed_劇本監督.png"
	original_board(background_file)
	pygame.time.delay(intro_delay_time)
	original_board(background_file)
	change_background("ed_劇本監督.png", "ed_人設.png", intro_change_speed)

	background_file = "ed_人設.png"
	original_board(background_file)
	pygame.time.delay(intro_delay_time)
	original_board(background_file)
	change_background("ed_人設.png", "ed_美術設計.png", intro_change_speed)
	
	background_file = "ed_美術設計.png"
	original_board(background_file)
	pygame.time.delay(intro_delay_time)
	original_board(background_file)
	change_background("ed_美術設計.png", "ed_畫面濾鏡.png", intro_change_speed)
	
	background_file = "ed_畫面濾鏡.png"
	original_board(background_file)
	pygame.time.delay(intro_delay_time)
	original_board(background_file)
	change_background("ed_畫面濾鏡.png", "ed_作畫監督.png", intro_change_speed)

	background_file = "ed_作畫監督.png"
	original_board(background_file)
	pygame.time.delay(intro_delay_time)
	original_board(background_file)
	change_background("ed_作畫監督.png", "ed_程式架構.png", intro_change_speed)

	background_file = "ed_程式架構.png"
	original_board(background_file)
	pygame.time.delay(intro_delay_time)
	original_board(background_file)
	change_background("ed_程式架構.png", "ed_程式功能.png", intro_change_speed)

	background_file = "ed_程式功能.png"
	original_board(background_file)
	pygame.time.delay(intro_delay_time)
	original_board(background_file)
	change_background("ed_程式功能.png", "ed_程式設計.png", intro_change_speed)

	background_file = "ed_程式設計.png"
	original_board(background_file)
	pygame.time.delay(intro_delay_time)
	original_board(background_file)
	change_background("ed_程式設計.png", "ed_網球遊戲.png", intro_change_speed)

	background_file = "ed_網球遊戲.png"
	original_board(background_file)
	pygame.time.delay(intro_delay_time)
	original_board(background_file)
	change_background("ed_網球遊戲.png", "ed_遊戲測試.png", intro_change_speed)

	background_file = "ed_遊戲測試.png"
	original_board(background_file)
	pygame.time.delay(intro_delay_time)
	original_board(background_file)
	change_background("ed_遊戲測試.png", "ed_oblivious.png", intro_change_speed)
	
	background_file = "ed_oblivious.png"
	original_board(background_file)
	pygame.time.delay(intro_delay_time)
	original_board(background_file)
	change_background("ed_oblivious.png", "ed_sinners.png", intro_change_speed)
	
	background_file = "ed_sinners.png"
	original_board(background_file)
	pygame.time.delay(intro_delay_time)
	original_board(background_file)
	change_background("ed_sinners.png", "ed_m01.png", intro_change_speed)

	background_file = "ed_m01.png"
	original_board(background_file)
	pygame.time.delay(intro_delay_time)
	original_board(background_file)
	change_background("ed_m01.png", "ed_bgm.png", intro_change_speed)

	background_file = "ed_bgm.png"
	original_board(background_file)
	pygame.time.delay(intro_delay_time)
	original_board(background_file)
	change_background("ed_bgm.png", "ed_製作.png", intro_change_speed)

	background_file = "ed_製作.png"
	original_board(background_file)
	pygame.time.delay(intro_delay_time)
	original_board(background_file)
	change_background("ed_製作.png", "blackintro.png", intro_change_speed)
	
	background_file = "blackintro.png"
	original_board(background_file)
	change_background("blackintro.png", "ending.png", intro_change_speed)
	
	
	

	go_ed = False
	
	
	
	

data = list()

gameExit = False
x = 0	
par = 0
chapter_pointer = 1

choice = 0
z = 0

playmusic1 = True
playmusic1_2 = True
playmusic2 = True
playmusic3 = True
playmusic4 = True
play_ed = True
fade_out = True

goch1 = True
goch2 = True
goch3 = True
goch4 = True
goch5 = True
goch8 = True
go_ed = True
	
musicfrom = 0.000
nowplaying = ""
				



pygame.mixer.music.load("sinners.wav")
nowplaying = "sinners.wav"

pygame.mixer.music.load(nowplaying)
pygame.mixer.music.play(-1, musicfrom)

#game opening
#opening()
				

background_file = "start.png"
background = pygame.image.load(background_file).convert()

original_board(background_file)
loading()
#main loop

original_board(background_file)
pygame.display.flip()

print(musicfrom)	




while not gameExit:
	clock.tick(60)
	
	
	
	if x > theblock_for_changing_background:
		x = theblock_for_changing_background - 1
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				saving()
			if event.key == pygame.K_d:
				x += 1
			if event.key == pygame.K_a:
				x -= 1
				if x < 0:
					x = 0
	


	
	#game logic
	if chapter_pointer == 1 and goch1 == True:	
		chapter_1()
	elif chapter_pointer == 1 and goch1 == False:
		x = 0
		par = 0
		chapter_pointer = 2
	
	
	if chapter_pointer == 2 and goch2 == True:
		chapter_2()
	elif chapter_pointer == 2 and goch2 == False:
		x = 0
		par = 0
		chapter_pointer = 3
	
	
	if chapter_pointer == 3 and goch3 == True:
		chapter_3()
	elif chapter_pointer == 3 and goch3 == False:
		x = 0
		par = 0
		chapter_pointer = 4
		
	
	
	if chapter_pointer == 4 and goch4 == True:
		chapter_4()
	elif chapter_pointer == 4 and goch4 == False:
		x = 0
		par = 0
		chapter_pointer = 8
		
	
	if chapter_pointer == 5 and goch5 == True:
		chapter_3()
	elif chapter_pointer == 5 and goch5 == False:
		x = 0
		par = 0
		chapter_pointer = 8
	
	
	if chapter_pointer == 8 and goch8 == True:
		chapter_8()
	elif chapter_pointer == 8 and goch8 == False:
		x = 0
		par = 0
		chapter_pointer = 9
		
	if chapter_pointer == 9 and go_ed == True:
		ending()
	elif chapter_pointer == 9 and go_ed == False:
		original_board("ending.png")
		
		

#test again




	
pygame.quit()
quit()