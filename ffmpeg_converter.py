import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess

encodable_file = '*.3g2;*.3gp;*.a64;*.ac3;*.ac4;*.adts;*.adx;*.aea;*.aiff;*.alaw;*.alp;*.amr;*.amv;*.apm;*.apng;*.aptx;*.aptx_hd;*.argo_asf;*.argo_cvg;*.asf;*.asf_stream;*.ass;*.ast;*.au;*.avi;*.avif;*.avm2;*.avs2;*.avs3;*.bit;*.caf;*.cavsvideo;*.codec2;*.codec2raw;*.crc;*.dash;*.data;*.daud;*.dfpwm;*.dirac;*.dnxhd;*.dts;*.dv;*.dvd;*.eac3;*.evc;*.f32be;*.f32le;*.f4v;*.f64be;*.f64le;*.ffmetadata;*.fifo;*.film_cpk;*.filmstrip;*.fits;*.flac;*.flv;*.framecrc;*.framehash;*.framemd5;*.g722;*.g723_1;*.g726;*.g726le;*.gif;*.gsm;*.gxf;*.h261;*.h263;*.h264;*.hash;*.hds;*.hevc;*.hls;*.iamf;*.ico;*.ilbc;*.image2;*.image2pipe;*.ipod;*.ircam;*.ismv;*.ivf;*.jacosub;*.kvag;*.latm;*.lrc;*.m4v;*.matroska;*.md5;*.microdvd;*.mjpeg;*.mkvtimestamp_v2;*.mlp;*.mmf;*.mov;*.mp2;*.mp3;*.mp4;*.mpeg;*.mpeg1video;*.mpeg2video;*.mpegts;*.mpjpeg;*.mulaw;*.mxf;*.mxf_d10;*.mxf_opatom;*.null;*.nut;*.obu;*.oga;*.ogg;*.ogv;*.oma;*.opus;*.psp;*.rawvideo;*.rcwt;*.rm;*.roq;*.rso;*.rtp;*.rtp_mpegts;*.rtsp;*.s16be;*.s16le;*.s24be;*.s24le;*.s32be;*.s32le;*.s8;*.sap;*.sbc;*.scc;*.sdl;*.sdl2;*.segment;*.smjpeg;*.smoothstreaming;*.sox;*.spdif;*.spx;*.srt;*.stream_segment;*.ssegment;*.streamhash;*.sup;*.svcd;*.swf;*.tee;*.truehd;*.tta;*.ttml;*.u16be;*.u16le;*.u24be;*.u24le;*.u32be;*.u32le;*.u8;*.uncodedframecrc;*.vc1;*.vc1test;*.vcd;*.vidc;*.vob;*.voc;*.vvc;*.w64;*.wav;*.webm;*.webm_chunk;*.webm_dash_manifest;*.webp;*.webvtt;*.wsaud;*.wtv;*.wv;*.yuv4mpegpipe'
decodable_file = '*.3dostr;*.4xm;*.aa;*.aac;*.aax;*.ac3;*.ac4;*.ace;*.acm;*.act;*.adf;*.adp;*.ads;*.adx;*.aea;*.afc;*.aiff;*.aix;*.alaw;*.alias_pix;*.alp;*.amr;*.amrnb;*.amrwb;*.anm;*.apac;*.apc;*.ape;*.apm;*.apng;*.aptx;*.aptx_hd;*.aqtitle;*.argo_asf;*.argo_brp;*.argo_cvg;*.asf;*.asf_o;*.ass;*.ast;*.au;*.av1;*.avi;*.avisynth;*.avr;*.avs;*.avs2;*.avs3;*.bethsoftvid;*.bfi;*.bfstm;*.bin;*.bink;*.binka;*.bit;*.bitpacked;*.bmp_pipe;*.bmv;*.boa;*.bonk;*.brender_pix;*.brstm;*.c93;*.caf;*.cavsvideo;*.cdg;*.cdxl;*.cine;*.codec2;*.codec2raw;*.concat;*.cri_pipe;*.dash;*.data;*.daud;*.dcstr;*.dds_pipe;*.derf;*.dfa;*.dfpwm;*.dhav;*.dirac;*.dnxhd;*.dpx_pipe;*.dsf;*.dshow;*.dsicin;*.dss;*.dts;*.dtshd;*.dv;*.dvbsub;*.dvbtxt;*.dxa;*.ea;*.ea_cdata;*.eac3;*.epaf;*.evc;*.exr_pipe;*.f32be;*.f32le;*.f64be;*.f64le;*.ffmetadata;*.film_cpk;*.filmstrip;*.fits;*.flac;*.flic;*.flv;*.frm;*.fsb;*.fwse;*.g722;*.g723_1;*.g726;*.g726le;*.g729;*.gdigrab;*.gdv;*.gem_pipe;*.genh;*.gif;*.gif_pipe;*.gsm;*.gxf;*.h261;*.h263;*.h264;*.hca;*.hcom;*.hdr_pipe;*.hevc;*.hls;*.hnm;*.iamf;*.ico;*.idcin;*.idf;*.iff;*.ifv;*.ilbc;*.image2;*.image2pipe;*.imf;*.ingenient;*.ipmovie;*.ipu;*.ircam;*.iss;*.iv8;*.ivf;*.ivr;*.j2k_pipe;*.jacosub;*.jpeg_pipe;*.jpegls_pipe;*.jpegxl_anim;*.jpegxl_pipe;*.jv;*.kux;*.kvag;*.laf;*.lavfi;*.libgme;*.libopenmpt;*.live_flv;*.lmlm4;*.loas;*.lrc;*.luodat;*.lvf;*.lxf;*.m4v;*.matroska;*.mca;*.mcc;*.mgsts;*.microdvd;*.mjpeg;*.mjpeg_2000;*.mlp;*.mlv;*.mm;*.mmf;*.mods;*.moflex;*.mov;*.mp4;*.m4a;*.3gp;*.3g2;*.mj2;*.mp3;*.mpc;*.mpc8;*.mpeg;*.mpegts;*.mpegtsraw;*.mpegvideo;*.mpjpeg;*.mpl2;*.mpsub;*.msf;*.msnwctcp;*.msp;*.mtaf;*.mtv;*.mulaw;*.musx;*.mv;*.mvi;*.mxf;*.mxg;*.nc;*.nistsphere;*.nsp;*.nsv;*.nut;*.nuv;*.obu;*.ogg;*.oma;*.osq;*.paf;*.pam_pipe;*.pbm_pipe;*.pcx_pipe;*.pdv;*.pfm_pipe;*.pgm_pipe;*.pgmyuv_pipe;*.pgx_pipe;*.phm_pipe;*.photocd_pipe;*.pictor_pipe;*.pjs;*.pmp;*.png_pipe;*.pp_bnk;*.ppm_pipe;*.psd_pipe;*.psxstr;*.pva;*.pvf;*.qcp;*.qdraw_pipe;*.qoa;*.qoi_pipe;*.r3d;*.rawvideo;*.realtext;*.redspark;*.rka;*.rl2;*.rm;*.roq;*.rpl;*.rsd;*.rso;*.rtp;*.rtsp;*.s16be;*.s16le;*.s24be;*.s24le;*.s32be;*.s32le;*.s337m;*.s8;*.sami;*.sap;*.sbc;*.sbg;*.scc;*.scd;*.sdns;*.sdp;*.sdr2;*.sds;*.sdx;*.ser;*.sga;*.sgi_pipe;*.shn;*.siff;*.simbiosis_imx;*.sln;*.smjpeg;*.smk;*.smush;*.sol;*.sox;*.spdif;*.srt;*.stl;*.subviewer;*.subviewer1;*.sunrast_pipe;*.sup;*.svag;*.svg_pipe;*.svs;*.swf;*.tak;*.tedcaptions;*.thp;*.tiertexseq;*.tiff_pipe;*.tmv;*.truehd;*.tta;*.tty;*.txd;*.ty;*.u16be;*.u16le;*.u24be;*.u24le;*.u32be;*.u32le;*.u8;*.usm;*.v210;*.v210x;*.vag;*.vbn_pipe;*.vc1;*.vc1test;*.vfwcap;*.vidc;*.vividas;*.vivo;*.vmd;*.vobsub;*.voc;*.vpk;*.vplayer;*.vqf;*.vvc;*.w64;*.wady;*.wav;*.wavarc;*.wc3movie;*.webm_dash_manifest;*.webp_pipe;*.webvtt;*.wsaud;*.wsd;*.wsvqa;*.wtv;*.wv;*.wve;*.xa;*.xbin;*.xbm_pipe;*.xmd;*.xmv;*.xpm_pipe;*.xvag;*.xwd_pipe;*.xwma;*.yop;*.yuv4mpegpipe'


class VideoConverterApp:
	def __init__(self, root):
		self.root = root
		self.root.title('音视频转换器')
		self.root.resizable(False, False)
		
		self.width = 50
		
		self.input_file = ''
		self.output_file = ''
		
		self.create_widgets()
	
	def create_widgets(self):
		# 输入文件选择
		self.input_label = tk.Label(self.root, text='输入音视频文件:')
		self.input_label.pack(pady=5, anchor=tk.W)
		self.input_entry = tk.Entry(self.root, width=self.width)
		self.input_entry.pack(pady=5, anchor=tk.W)
		self.browse_button = tk.Button(self.root, text='浏览', command=self.browse_input)
		self.browse_button.pack(pady=5)
		
		# 输出文件选择
		self.output_label = tk.Label(self.root, text='输出音视频文件:')
		self.output_label.pack(pady=5, anchor=tk.W)
		self.output_entry = tk.Entry(self.root, width=self.width)
		self.output_entry.pack(pady=5, anchor=tk.W)
		self.output_button = tk.Button(self.root, text='浏览', command=self.browse_output)
		self.output_button.pack(pady=5)
		
		# 清晰度选项
		self.resolution_var = tk.BooleanVar()
		self.resolution_check = tk.Checkbutton(self.root, text='清晰度：', variable=self.resolution_var,
		                                       command=self.toggle_resolution)
		self.resolution_check.pack(pady=5, anchor=tk.W)
		self.resolution_options = {'360P': '640:-1', '480P': '852:-1', '720P': '1280:-1', '1080P': '1920:-1',
		                           '2K': '2560:-1', '4K': '3840:-1'}
		self.resolution_value = tk.StringVar(value='1080P')
		self.resolution_entry = tk.OptionMenu(root, self.resolution_value, *self.resolution_options.keys())
		self.resolution_entry.pack(pady=5)
		self.resolution_entry.config(state='disabled')
		
		# 起始时间
		self.start_var = tk.BooleanVar()
		self.start_check = tk.Checkbutton(self.root, text='起始时间（HH:MM:SS格式或秒数）：', variable=self.start_var,
		                                  command=self.toggle_start)
		self.start_check.pack(pady=5, anchor=tk.W)
		self.start_entry = tk.Entry(self.root, width=self.width)
		self.start_entry.pack(pady=5, anchor=tk.W)
		self.start_entry.config(state='disabled')
		
		# 结束时间
		self.end_var = tk.BooleanVar()
		self.end_check = tk.Checkbutton(self.root, text='结束时间（HH:MM:SS格式或秒数）：', variable=self.end_var,
		                                command=self.toggle_end)
		self.end_check.pack(pady=5, anchor=tk.W)
		self.end_entry = tk.Entry(self.root, width=self.width)
		self.end_entry.pack(pady=5, anchor=tk.W)
		self.end_entry.config(state='disabled')
		
		# 编码器选项
		self.codec_var = tk.BooleanVar()
		self.codec_check = tk.Checkbutton(self.root, text='编码器：', variable=self.codec_var,
		                                  command=self.toggle_codec)
		self.codec_check.pack(pady=5, anchor=tk.W)
		self.codec_options = {
			'（视频）H.264': 'libx264',
			'（视频）H.265': 'libx265',
			'（视频）MPEG-2': 'mpeg2video',
			'（视频）MPEG-4': 'mpeg4',
			'（视频）VP8': 'libvpx',
			'（视频）VP9': 'libvpx-vp9',
			'（视频）AV1': 'libaom-av1',
			'（视频）ProRes': 'prores',
			'（视频）DNxHD': 'dnxhd',

			# '（音频）AAC': 'aac',
			# '（音频）MP3': 'mp3',
			# '（音频）WAV S16le': 'pcm_s16le',
			# '（音频）WAV S24le': 'pcm_s24le',
			# '（音频）FLAC': 'flac',
			# '（音频）OGG Vorbis': 'libvorbis',
			# '（音频）AC3': 'ac3',
			# '（音频）Opus': 'libopus',
			# '（音频）ALAC': 'alac'
		}
		self.codec_value = tk.StringVar(value='（视频）H.264')
		self.codec_entry = tk.OptionMenu(root, self.codec_value, *self.codec_options.keys())
		self.codec_entry.pack(pady=5)
		self.codec_entry.config(state='disabled')
		
		# 帧率选项
		self.fps_var = tk.BooleanVar()
		self.fps_check = tk.Checkbutton(self.root, text='帧率（fps）:', variable=self.fps_var,
		                                command=self.toggle_fps)
		self.fps_check.pack(pady=5, anchor=tk.W)
		self.fps_entry = tk.Entry(self.root, width=self.width)
		self.fps_entry.insert(0, '25')
		self.fps_entry.pack(pady=5, anchor=tk.W)
		self.fps_entry.config(state='disabled')
		
		# 视频码率选项
		self.video_code_rate_var = tk.BooleanVar()
		self.video_code_rate_check = tk.Checkbutton(self.root, text='视频码率（Kbps）:',
		                                            variable=self.video_code_rate_var,
		                                            command=self.toggle_video_code_rate)
		self.video_code_rate_check.pack(pady=5, anchor=tk.W)
		self.video_code_rate_entry = tk.Entry(self.root, width=self.width)
		self.video_code_rate_entry.pack(pady=5, anchor=tk.W)
		self.video_code_rate_entry.insert(0, '2000')
		self.video_code_rate_entry.config(state='disabled')
		
		# 音频码率选项
		self.audio_code_rate_var = tk.BooleanVar()
		self.audio_code_rate_check = tk.Checkbutton(self.root, text='音频码率（Kbps）:',
		                                            variable=self.audio_code_rate_var,
		                                            command=self.toggle_audio_code_rate)
		self.audio_code_rate_check.pack(pady=5, anchor=tk.W)
		self.audio_code_rate_entry = tk.Entry(self.root, width=self.width)
		self.audio_code_rate_entry.pack(pady=5, anchor=tk.W)
		self.audio_code_rate_entry.insert(0, '128')
		self.audio_code_rate_entry.config(state='disabled')
		
		# 转换按钮
		self.convert_button = tk.Button(self.root, text='转换', command=self.convert_video)
		self.convert_button.pack(pady=20)
	
	def browse_input(self):
		i = filedialog.askopenfilename(
			filetypes=[('可解码音视频文件', decodable_file), ('所有文件', '*.*')])
		if i != '':
			self.input_file = i
		self.input_entry.delete(0, tk.END)
		self.input_entry.insert(0, self.input_file)
	
	def browse_output(self):
		i = filedialog.asksaveasfilename(defaultextension='.mp4',
		                                 filetypes=[('可解码音视频文件', encodable_file),
		                                            ('所有文件', '*.*')])
		if i != '':
			self.output_file = i
		self.output_entry.delete(0, tk.END)
		self.output_entry.insert(0, self.output_file)
	
	def toggle_resolution(self):
		if self.resolution_var.get():
			self.resolution_entry.config(state='normal')
		else:
			self.resolution_entry.config(state='disabled')
	
	def toggle_start(self):
		if self.start_var.get():
			self.start_entry.config(state='normal')
		else:
			self.start_entry.config(state='disabled')
	
	def toggle_end(self):
		if self.end_var.get():
			self.end_entry.config(state='normal')
		else:
			self.end_entry.config(state='disabled')
	
	def toggle_codec(self):
		if self.codec_var.get():
			self.codec_entry.config(state='normal')
		else:
			self.codec_entry.config(state='disabled')
	
	def toggle_fps(self):
		if self.fps_var.get():
			self.fps_entry.config(state='normal')
		else:
			self.fps_entry.config(state='disabled')
	
	def toggle_video_code_rate(self):
		if self.video_code_rate_var.get():
			self.video_code_rate_entry.config(state='normal')
		else:
			self.video_code_rate_entry.config(state='disabled')
	
	def toggle_audio_code_rate(self):
		if self.audio_code_rate_var.get():
			self.audio_code_rate_entry.config(state='normal')
		else:
			self.audio_code_rate_entry.config(state='disabled')
	
	def convert_video(self):
		if not self.input_file or not self.output_file:
			messagebox.showerror('错误', '请指定输入和输出文件！')
			return
		
		command = ['ffmpeg', '-y', '-i', self.input_file]
		
		if self.start_var.get():
			start_time = self.start_entry.get()
			command += ['-ss', start_time]
		
		if self.end_var.get():
			end_time = self.end_entry.get()
			command += ['-to', end_time]
		
		if self.resolution_var.get():
			resolution = self.resolution_value.get()
			command += ['-vf', f'scale={self.resolution_options[resolution]}']
		
		if self.codec_var.get():
			codec = self.codec_value.get()
			command += ['-c:v', self.codec_options[codec]]
		
		if self.fps_var.get():
			fps = self.fps_entry.get()
			command += ['-r', fps]
		
		if self.video_code_rate_var.get():
			vcr = self.video_code_rate_entry.get() + 'k'
			command += ['-b:v', vcr]
		
		if self.audio_code_rate_var.get():
			acr = self.audio_code_rate_entry.get() + 'k'
			command += ['-b:a', acr]
		
		command.append(self.output_file)
		
		try:
			subprocess.run(command, check=True)
			messagebox.showinfo('成功', '音视频转换成功！')
		except subprocess.CalledProcessError as e:
			messagebox.showerror('错误', f'转换失败：{e}')


if __name__ == '__main__':
	root = tk.Tk()
	app = VideoConverterApp(root)
	root.mainloop()
