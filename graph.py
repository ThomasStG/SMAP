import numpy as np
import time

INF = 99999
t = time.time()

n = np.zeros((171, 171))
n[0, 1] = 216
n[0, 2] = 140

n[1, 0] = 216
n[1, 3] = 220

n[2, 0] = 140
n[2, 3] = 325
n[2, 4] = 183

n[3, 1] = 220
n[3, 2] = 325
n[3, 5] = 222

n[4, 2] = 183
n[4, 6] = 200
n[4, 7] = 225

n[5, 3] = 222
n[5, 8] = 200

n[6, 4] = 200
n[6, 9] = 114
n[6, 10] = 136

n[7, 4] = 225
n[7, 11] = 200
n[7, 12] = 400
n[7, 13] = 145

n[8, 5] = 200
n[8, 14] = 388
n[8, 32] = 199
n[8, 29] = 366

n[9, 6] = 114
n[9, 15] = 51

n[10, 6] = 136
n[10, 11] = 133  # This is New Castle

n[11, 10] = 133
n[11, 7] = 200
n[11, 16] = 147

n[12, 7] = 400
n[12, 17] = 362
n[12, 18] = 80

n[13, 7] = 145
n[13, 19] = 184
n[13, 20] = 291

n[14, 8] = 388
n[14, 21] = 221
n[14, 22] = 202

n[15, 9] = 51
n[15, 16] = 272
n[15, 23] = 309

n[16, 11] = 147
n[16, 15] = 272
n[16, 24] = 408

n[17, 12] = 362
n[17, 20] = 168
n[17, 25] = 240
n[17, 26] = 361

n[18, 12] = 80
n[18, 27] = 88
n[18, 28] = 86

n[19, 13] = 184
n[19, 29] = 75  # Parking
n[19, 30] = 417

n[20, 13] = 291
n[20, 17] = 168
n[20, 31] = 370  # Kingston

n[21, 14] = 221
n[21, 32] = 112
n[21, 33] = 100
n[21, 34] = 120

n[22, 14] = 202
n[22, 35] = 71
n[22, 36] = 96

n[23, 15] = 309

n[24, 16] = 408  # Athletic Center
n[24, 37] = 60

n[25, 17] = 240
n[25, 38] = 40
n[25, 39] = 77

n[26, 17] = 361
n[26, 40] = 73
n[26, 41] = 199

n[27, 18] = 88
n[27, 28] = 54
n[27, 42] = 130
n[27, 43] = 123

n[28, 18] = 86
n[28, 27] = 54
n[28, 44] = 155
n[28, 45] = 155

n[29, 19] = 75
n[29, 8] = 366

n[30, 19] = 417
n[30, 33] = 71

n[31, 20] = 370
n[31, 33] = 78
n[31, 34] = 150
n[31, 40] = 156

n[32, 21] = 112
n[32, 33] = 100
n[32, 8] = 199

n[33, 21] = 100
n[33, 30] = 71
n[33, 31] = 78
n[33, 32] = 100

n[34, 21] = 120
n[34, 31] = 150
n[34, 40] = 136
n[34, 57] = 120
n[34, 168] = 100

n[35, 22] = 71
n[35, 36] = 71

n[36, 22] = 96
n[36, 35] = 71
n[36, 46] = 215
n[36, 47] = 130

n[37, 24] = 60
n[37, 44] = 147
n[37, 48] = 103

n[38, 25] = 40

n[39, 25] = 77
n[39, 41] = 230
n[39, 49] = 136
n[39, 50] = 172

n[40, 26] = 73
n[40, 31] = 156
n[40, 34] = 136
n[40, 51] = 146

n[41, 26] = 199
n[41, 39] = 230
n[41, 50] = 318
n[41, 52] = 93

n[42, 27] = 130
n[42, 49] = 120

n[43, 27] = 123
n[43, 53] = 60
n[43, 54] = 50
n[43, 55] = 242

n[44, 28] = 155
n[44, 37] = 147
n[44, 45] = 55

n[45, 28] = 155
n[45, 44] = 55
n[45, 56] = 274

n[46, 36] = 215
n[46, 57] = 83
n[46, 58] = 98
n[46, 168] = 124

n[47, 36] = 130
n[47, 59] = 114
n[47, 60] = 450

n[48, 37] = 103
n[48, 61] = 329
n[48, 62] = 113

n[49, 39] = 136
n[49, 42] = 120
n[49, 50] = 250
n[49, 63] = 62
n[49, 64] = 127

n[50, 39] = 172
n[50, 41] = 318
n[50, 49] = 250
n[50, 67] = 56

n[51, 40] = 146
n[51, 52] = 48
n[51, 57] = 134
n[51, 65] = 150

n[52, 41] = 93
n[52, 51] = 48
n[52, 66] = 236

n[53, 43] = 60

n[54, 43] = 50

n[55, 43] = 242
n[55, 56] = 180

n[56, 45] = 274
n[56, 48] = 229
n[56, 169] = 45

n[57, 34] = 120
n[57, 46] = 83
n[57, 51] = 134

n[58, 46] = 98
n[58, 79] = 283

n[59, 47] = 114

n[60, 47] = 450
n[60, 68] = 50

n[61, 48] = 329
n[61, 62] = 50

n[62, 48] = 113
n[62, 61] = 50
n[62, 69] = 115

n[63, 49] = 62

n[64, 49] = 127
n[64, 67] = 235

n[65, 51] = 150
n[65, 71] = 130

n[66, 52] = 236
n[66, 72] = 134
n[66, 73] = 185
n[66, 74] = 238

n[67][50] = 36
n[67][64] = 235
n[67][70] = 36

n[169, 56] = 45
n[169, 69] = 83
n[169, 75] = 73

n[68, 60] = 50
n[68, 76] = 226

n[69, 62] = 115
n[69, 169] = 83

n[70, 67] = 36
n[70, 73] = 139
n[70, 77] = 81
n[70, 78] = 50

n[71, 65] = 130
n[71, 72] = 45

n[72, 71] = 45
n[72, 66] = 134
n[72, 79] = 227
n[72, 80] = 112
n[72, 81] = 97

n[73, 66] = 185
n[73, 70] = 139
n[73, 78] = 139

n[74, 66] = 238
n[74, 82] = 100
n[74, 83] = 98

n[75, 169] = 73
n[75, 84] = 117
n[75, 85] = 294

n[76, 68] = 226
n[76, 86] = 88
n[76, 87] = 76
n[76, 88] = 113

n[77, 70] = 81
n[77, 89] = 70
n[77, 90] = 170

n[78, 70] = 50
n[78, 73] = 139
n[78, 89] = 36
n[78, 91] = 272
n[78, 92] = 135

n[79, 72] = 227
n[79, 93] = 254
n[79, 94] = 592
n[79, 58] = 283

n[80, 72] = 112
n[80, 81] = 40

n[81, 72] = 97
n[81, 80] = 40
n[81, 82] = 175

n[82, 74] = 100
n[82, 81] = 175
n[82, 83] = 215

n[83, 74] = 98
n[83, 82] = 215
n[83, 91] = 300

n[84, 75] = 117
n[84, 95] = 52
n[84, 96] = 33

n[85, 75] = 294
n[85, 97] = 42
n[85, 98] = 203

n[86, 76] = 88

n[87, 76] = 76
n[87, 99] = 82

n[88, 76] = 113
n[88, 100] = 120
n[88, 101] = 160

n[89, 77] = 70
n[89, 78] = 36

n[90, 77] = 170
n[90, 103] = 42

n[91, 78] = 272
n[91, 83] = 300
n[91, 104] = 366
n[91, 105] = 59

n[92, 78] = 135
n[92, 117] = 1

n[93, 79] = 254
n[93, 106] = 348

n[94, 79] = 592
n[94, 107] = 68
n[94, 108] = 236

n[95, 84] = 52
n[95, 96] = 56
n[95, 109] = 200

n[96, 84] = 33
n[96, 95] = 56
n[96, 110] = 302
n[96, 111] = 93

n[97, 85] = 42

n[98, 85] = 203
n[98, 110] = 220
n[98, 112] = 211
n[98, 113] = 648

n[99, 87] = 82
n[99, 100] = 180
n[99, 114] = 50

n[100, 88] = 120
n[100, 99] = 80
n[100, 115] = 150
# 49 more nodes unlabeled-> 64 more nodes to write down
n[101, 88] = 160


n[102, 103] = 69
n[102, 109] = 69

n[103, 90] = 42
n[103, 128] = 32

n[104, 91] = 366
n[104, 118] = 50
n[104, 119] = 113

n[105, 91] = 59
n[105, 120] = 347
n[105, 121] = 136

n[106, 93] = 348
n[106, 114] = 230
n[106, 122] = 180

n[107, 94] = 68
n[107, 123] = 140

n[108, 94] = 236
n[108, 124] = 228
n[108, 125] = 153
n[108, 126] = 324

n[109, 95] = 200
n[109, 102] = 69
n[109, 127] = 46

n[110, 96] = 302
n[110, 98] = 220
n[110, 119] = 129

n[111, 96] = 93

n[112, 98] = 211
n[112, 119] = 229
n[112, 130] = 63
n[112, 129] = 141

n[113, 98] = 648

n[114, 99] = 50
n[114, 106] = 230

n[115, 100] = 150

n[116, 120] = 263
n[116, 121] = 159

n[117, 92] = 1
n[117, 128] = 168

n[118, 104] = 50
n[118, 127] = 185
n[118, 128] = 97

n[119, 104] = 113
n[119, 110] = 126
n[119, 112] = 229

n[120, 105] = 347
n[120, 116] = 263
n[120, 131] = 140

n[121, 105] = 136
n[121, 116] = 159
n[121, 132] = 192

n[122, 106] = 180
n[122, 133] = 100

n[123, 107] = 140
n[123, 133] = 386
n[123, 134] = 134

n[124, 108] = 228
n[124, 135] = 337

n[125, 108] = 153
n[125, 136] = 139
n[125, 137] = 270

n[126, 108] = 324
n[126, 138] = 60
n[126, 139] = 105
n[126, 140] = 323

n[127, 109] = 46
n[127, 118] = 185

n[128, 103] = 32
n[128, 117] = 168
n[128, 118] = 97

n[129, 112] = 141
n[129, 132] = 102
n[129, 141] = 184

n[130, 112] = 63

n[131, 120] = 140
n[131, 142] = 160
n[131, 143] = 84

n[132, 121] = 192
n[132, 129] = 102
n[132, 144] = 236

n[133, 122] = 100
n[133, 123] = 386

n[134, 123] = 134

n[135, 124] = 337
n[135, 145] = 188

n[136, 125] = 139
n[136, 170] = 156
n[136, 146] = 132

n[137, 125] = 270
n[137, 143] = 177

n[138, 126] = 60
n[138, 170] = 169
n[138, 147] = 230

n[139, 126] = 105
n[139, 148] = 344
n[139, 149] = 496

n[140, 126] = 323
n[140, 145] = 100
n[140, 150] = 313

n[141, 129] = 184
n[141, 144] = 121
n[141, 151] = 137

n[142, 131] = 160
n[142, 148] = 175
n[142, 152] = 408

n[143, 137] = 177
n[143, 131] = 84
n[143, 146] = 136

n[144, 132] = 236
n[144, 141] = 121
n[144, 151] = 198

n[145, 135] = 188
n[145, 140] = 100
n[145, 153] = 238

n[146, 136] = 132
n[146, 143] = 136
n[146, 147] = 160

n[147, 138] = 230
n[147, 146] = 160

n[148, 139] = 344
n[148, 142] = 175
n[148, 154] = 144

n[149, 139] = 496
n[149, 155] = 224
n[149, 156] = 319

n[150, 140] = 313
n[150, 153] = 182

n[151, 141] = 137
n[151, 144] = 198
n[151, 157] = 71

n[152, 142] = 408
n[152, 155] = 274
n[152, 158] = 200

n[153, 145] = 238
n[153, 150] = 182

n[154, 148] = 144
n[154, 155] = 238
n[154, 158] = 142

n[155, 149] = 224
n[155, 152] = 274
n[155, 154] = 238

n[156, 149] = 319
n[156, 159] = 188
n[156, 160] = 631

n[157, 151] = 71

n[158, 152] = 200
n[158, 154] = 142

n[159, 151] = 473
n[159, 156] = 188

n[160, 156] = 631
n[160, 161] = 31
n[160, 162] = 423

n[161, 160] = 31
n[161, 163] = 89

n[162, 160] = 423
n[162, 164] = 499
n[162, 165] = 1666

n[163, 161] = 89
n[163, 166] = 76
n[163, 164] = 355

n[164, 163] = 355
n[164, 162] = 499
n[164, 167] = 442

n[165, 162] = 1666

n[166, 163] = 76

n[167, 164] = 442

n[168, 34] = 100
n[168, 46] = 124

n[169, 56] = 45
n[169, 69] = 83
n[169, 75] = 73

n[170, 136] = 156
n[170, 138] = 169

for i in range(171):
    for j in range(171):
        if n[i,j] == 0:
            n[i,j] = INF

np.save('./static/other/map.npy', n)
elapsed = time.time() - t
print(elapsed)
"""

coordinates = np.array(
[(-71.457512, 43.040871),
(-71.45694, 43.041336),
(-71.456993, 43.040775),
(-71.456177, 43.041428),
(-71.45649, 43.040382),
(-71.455276, 43.041481),
(-71.456985, 43.039986),
(-71.455833, 43.040047),
(-71.454628, 43.041641),
(-71.457268, 43.039677),
(-71.456589, 43.039703),
(-71.456184, 43.039536),
(-71.454597, 43.039375),
(-71.455536, 43.040382),
(-71.453316, 43.042149),
(-71.457176, 43.039532),
(-71.45636, 43.03915),
(-71.45401, 43.040272),
(-71.454366,43.039256),###
(-71.4552, 43.040798),
(-71.454514, 43.040569),
(-71.453522, 43.041637),
(-71.45253, 43.042068),
(-71.456604, 43.03875),
(-71.455177, 43.038395),
(-71.453506, 43.040031),
(-71.45356, 43.04084),
(-71.454074,43.039088),###
(-71.454018, 43.039093),
(-71.454247, 43.038994),
(-71.455467, 43.040962),
(-71.454056, 43.041618),
(-71.453743, 43.041363),
(-71.453781, 43.041828),
(-71.453781, 43.041607),
(-71.453102, 43.041359),
(-71.452507, 43.041851),
(-71.452225, 43.041973),
(-71.454857, 43.038372),
(-71.453491, 43.040207),
(-71.453217, 43.039936),
(-71.453392, 43.041019),
(-71.452904, 43.040531),
(-71.453789, 43.039364),
(-71.453751, 43.038883),
(-71.45472, 43.038731),
(-71.454506, 43.038612),
(-71.452644, 43.041405),
(-71.452141, 43.042271),
(-71.454674, 43.038086),
(-71.453468, 43.039646),
(-71.452721, 43.039734),
(-71.452896, 43.04092),
(-71.452728, 43.040802),
(-71.453613, 43.039032),
(-71.453857, 43.038799),
(-71.453712, 43.038368),
(-71.453957, 43.038002),
(-71.452759, 43.041203),
(-71.452377, 43.041508),
(-71.452583, 43.042458),
(-71.451309, 43.043285),
(-71.454536, 43.037712),
(-71.454407, 43.037884),
(-71.453987, 43.03949),
(-71.453262, 43.03936),
(-71.452301, 43.040932),
(-71.452003, 43.040531),
(-71.45253, 43.03965),
(-71.451248, 43.043427),
(-71.454109, 43.037701),
(-71.452423, 43.039612),
(-71.451881, 43.040802),
(-71.451736, 43.040775),
(-71.452187, 43.039925),
(-71.451172, 43.040184),
(-71.453712, 43.037781),
(-71.450783, 43.043709),
(-71.452492, 43.039375),
(-71.452209, 43.039543),
(-71.451439, 43.041378),
(-71.451324, 43.040722),
(-71.451424, 43.040619),
(-71.450821, 43.040356),
(-71.450958, 43.039822),
(-71.453522, 43.038071),
(-71.452774, 43.037403),
(-71.450928, 43.043747),
(-71.450546, 43.043652),
(-71.450607, 43.043983),
(-71.452232, 43.03944),
(-71.452812, 43.038956),
(-71.451355, 43.039188),
(-71.451881, 43.039181),
(-71.451172, 43.041973),
(-71.449287, 43.041111),
(-71.453423, 43.038197),
(-71.4534, 43.038036),
(-71.452744, 43.037201),
(-71.452065, 43.03756),
(-71.450317, 43.043568),
(-71.450119, 43.043991),
(-71.450836, 43.044159),
(-71.45295, 43.038822),
(-71.452721, 43.038849),
(-71.452148, 43.038559),
(-71.451096, 43.03915),
(-71.450508, 43.04285),
(-71.449219, 43.041386),
(-71.448425, 43.040867),
(-71.453087, 43.03867),
(-71.4524, 43.037998),
(-71.453041, 43.037945),
(-71.451447, 43.037861),
(-71.450317, 43.036251),
(-71.450134, 43.043468),
(-71.44957, 43.044044),
(-71.450409, 43.038834),
(-71.451973, 43.038933),
(-71.452469, 43.038605),
(-71.452065, 43.038235),
(-71.449844, 43.039387),
(-71.450935, 43.038792),
(-71.44973, 43.04245),
(-71.449654, 43.041489),
(-71.447769, 43.041008),
(-71.448944, 43.040638),
(-71.447594, 43.040318),
(-71.453003, 43.038479),
(-71.452576, 43.038864),
(-71.45092, 43.038071),
(-71.451302, 43.037704),
(-71.449524, 43.0396),
(-71.451027, 43.038368),
(-71.449539, 43.042088),
(-71.449318, 43.041824),
(-71.446579, 43.040592),
(-71.448891, 43.040245),
(-71.449455, 43.040302),
(-71.447701, 43.040165),
(-71.447289, 43.040016),
(-71.446625, 43.040031),
(-71.450218, 43.038086),
(-71.448875, 43.039436),
(-71.449364, 43.039913),
(-71.450127, 43.038479),
(-71.446304, 43.040249),
(-71.448883, 43.039909),
(-71.448318, 43.039883),
(-71.448257, 43.039509),
(-71.447052, 43.038788),
(-71.445633, 43.039955),
(-71.449738, 43.037991),
(-71.4487, 43.038654),
(-71.445625, 43.040359),
(-71.44809, 43.039162),
(-71.447662, 43.038658),
(-71.447479, 43.037785),
(-71.449905, 43.037846),
(-71.448685, 43.039173),
(-71.448112, 43.037594),
(-71.446022, 43.036484),
(-71.445915, 43.036564),
(-71.444801, 43.035725),
(-71.44561, 43.036526),
(-71.444382, 43.036915),
(-71.442413, 43.033028),
(-71.445831, 43.036636),
(-71.444107, 43.037579),
(-71.452934, 43.041603),
(-71.453934, 43.03788)])
np.save('coordinates.npy', coordinates)"""
