import os.path


os.system("ffplay -flags2 +export_mvs -i Resistencia_BM19_cropped.mp4 -vf codecview=mv=pf+bf+bb")
#os.system("ffmpeg -flags2 +export_mvs -i /Users/edwjunior/Documents/UNIVERSIDAD/4o\ CURSO/1r\ TRIMESTRE/SISTEMES\ DE\ "
          #"CODIFICACIÓ\ D\'ÀUDIO\ I\ VIDEO/LABS/LAB2-VideoPart/Resistencia_BM19_cropped.mp4 -vf codecview=mv=pf+bf+bb output.mp4")
