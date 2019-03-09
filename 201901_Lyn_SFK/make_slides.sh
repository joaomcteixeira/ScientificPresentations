#! /bin/bash

clear

rm *.pdf

python /home/joao/Programming/presentationplotlib/gen_slides.py \
    \
sld_0.py    \
sld_joao.py \
sld_1.py    \
sld_sfks_intro_0.py   \
sld_sfks_intro_1.py \
sld_sfks_intro_2.py \
sld_sfks_intro_3.py \
sld_sfks_intro_4.py \
sld_sfks_intro_5.py \
sld_sfks_highlight.py   \
sld_sfks_titulares_1.py \
sld_sfks_titulares_2.py \
sld_sfks_titulares_3.py \
sld_sfks_titulares_4.py \
sld_sfks_titulares_5.py \
sld_sfks_titulares_total.py \
sld_sfks_intro_5.py \
sld_sfks_intro_6.py \
sld_lyn_main.py \
sld_lyn_presentation_0.py   \
sld_lyn_presentation_1.py   \
sld_lyn_presentation_2.py   \
sld_lyn_presentation_3.py   \
sld_lyn_presentation_4.py   \
sld_lyn_presentation_5.py   \
sld_lyn_presentation_6.py   \
sld_lyn_graphical_abs_0.py    \
sld_lyn_graphical_abs.py    \
sld_lyn_constructs_0.py \
sld_lyn_constructs_1.py \
sld_lyn_constructs_2.py \
sld_lyn_assignment_0.py \
sld_lyn_assignment_1.py \
sld_lyn_assignment_2.py \
sld_lyn_assignment_3.py \
sld_lyn_assignment_total.py \
sld_lyn_fig1_title.py   \
sld_lyn_fig1_1.py   \
sld_lyn_fig1_2.py   \
sld_lyn_fig1_3.py   \
sld_lyn_fig1_total.py   \
sld_lyn_fig1_conclusions.py   \
sld_lyn_fig1_conclusions_total.py   \
sld_lyn_uniques_0.py    \
sld_lyn_uniques_1.py    \
sld_lyn_uniques_2.py    \
sld_lyn_uniques_3.py    \
sld_lyn_uniques_total.py    \
sld_lyn_PRE_0.py    \
sld_lyn_PRE_1.py    \
sld_lyn_PRE_2.py    \
sld_lyn_PRE_total.py    \
sld_lyn_PPP_0.py    \
sld_lyn_PPP_1.py    \
sld_lyn_PPP_2.py    \
sld_lyn_PPP_3.py    \
sld_lyn_PPP_4.py    \
sld_lyn_PPP_5.py    \
sld_lyn_PPP_total.py    \
sld_lyn_final_conclusion_0.py \
sld_lyn_final_conclusion_1.py \
sld_lyn_final_conclusion_2.py   \
sld_lyn_agradecimientos_0.py \
sld_lyn_agradecimientos_1.py    \

pdfunite *.pdf presentation_lyn.pdf

rm page_*

exit 0
