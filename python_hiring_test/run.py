"""Main script for generating output.csv."""

# # # # # # # # # # # # # # # # # # # #
# David Ellenberger					  #
# python hiring test for Inside Edge  #
# April 2018						  #
# # # # # # # # # # # # # # # # # # # #

# TODO: add these to dependencies 
import csv
import numpy
import pandas

# TODO: add documentation / comments
def filter_min_AB(df, player_id, side):
	print((df[df['PitcherSide']=='R'].groupby('HitterId')['H'].sum()))

def main():
	# # # # # # # # # # # # # # # # # # #
    # Initialize our reqired dataframes # 
    # # # # # # # # # # # # # # # # # # #

    # Define our constants
    raw_csv_handle = './data/raw/pitchdata.csv'

    # Read in raw csv to a pandas dataframe
    raw_df = pandas.read_csv(raw_csv_handle)


    # # # # # # # # # # # # # # # # # # # # # #
    # Begin solving for specific combinations # 
    # # # # # # # # # # # # # # # # # # # # # # 

    # # #
    # Individual stats - Batting
    # # # 

    # Grab hitter's batting avg against righties
    avg_against_rhp = ((raw_df[raw_df['PitcherSide']=='R'].groupby('HitterId')['H'].sum()) \
    	/ (raw_df[raw_df['PitcherSide']=='R'].groupby('HitterId')['AB'].sum())).round(3)
    # I'm not sure who team 142 is, but they really could use more time in the cages...
    # Anyway, now against lefties
    avg_against_lhp = ((raw_df[raw_df['PitcherSide']=='L'].groupby('HitterId')['H'].sum()) \
    	/ (raw_df[raw_df['PitcherSide']=='L'].groupby('HitterId')['AB'].sum())).round(3)

    # Now we can create the intermediary dataframes from these series
    avg_against_rhp_df = avg_against_rhp.to_frame(name='Value')
    avg_against_rhp_df['Stat'] = 'AVG'
    avg_against_rhp_df['Split'] = 'vs RHP'
    avg_against_rhp_df['Subject'] = 'HitterId'
    avg_against_rhp_df['SubjectId'] = avg_against_rhp_df.index

    avg_against_lhp_df = avg_against_lhp.to_frame(name='Value')
    avg_against_lhp_df['Stat'] = 'AVG'
    avg_against_lhp_df['Split'] = 'vs LHP'
    avg_against_lhp_df['Subject'] = 'HitterId'
    avg_against_lhp_df['SubjectId'] = avg_against_lhp_df.index


    # OBP vs right handed
    # Apologizing in advance for the wall of brackets 
    # Find batters's OBP against righties - calculated as (hits + hbp + walks) / (total plate appearances)
    obp_against_rhp = (((raw_df[raw_df['PitcherSide']=='R'].groupby('HitterId')['H'].sum()) \
    	+ (raw_df[raw_df['PitcherSide']=='R'].groupby('HitterId')['BB'].sum()) \
    	+ (raw_df[raw_df['PitcherSide']=='R'].groupby('HitterId')['HBP'].sum())) \
    	/ ((raw_df[raw_df['PitcherSide']=='R'].groupby('HitterId')['AB'].sum()) \
    	+ (raw_df[raw_df['PitcherSide']=='R'].groupby('HitterId')['BB'].sum()) \
    	+ (raw_df[raw_df['PitcherSide']=='R'].groupby('HitterId')['HBP'].sum()) \
    	+ (raw_df[raw_df['PitcherSide']=='R'].groupby('HitterId')['SF'].sum()))).round(3)

    # Now for a batter's OBP against lefties
    obp_against_lhp = (((raw_df[raw_df['PitcherSide']=='L'].groupby('HitterId')['H'].sum()) \
    	+ (raw_df[raw_df['PitcherSide']=='L'].groupby('HitterId')['BB'].sum()) \
    	+ (raw_df[raw_df['PitcherSide']=='L'].groupby('HitterId')['HBP'].sum())) \
    	/ ((raw_df[raw_df['PitcherSide']=='L'].groupby('HitterId')['AB'].sum()) \
    	+ (raw_df[raw_df['PitcherSide']=='L'].groupby('HitterId')['BB'].sum()) \
    	+ (raw_df[raw_df['PitcherSide']=='L'].groupby('HitterId')['HBP'].sum()) \
    	+ (raw_df[raw_df['PitcherSide']=='L'].groupby('HitterId')['SF'].sum()))).round(3)

	# Create dataframes
    obp_against_rhp_df = obp_against_rhp.to_frame(name='Value')
    obp_against_rhp_df['Stat'] = 'OBP'
    obp_against_rhp_df['Split'] = 'vs RHP'
    obp_against_rhp_df['Subject'] = 'HitterId'
    obp_against_rhp_df['SubjectId'] = obp_against_rhp_df.index


    obp_against_lhp_df = obp_against_lhp.to_frame(name='Value')
    obp_against_lhp_df['Stat'] = 'OBP'
    obp_against_lhp_df['Split'] = 'vs LHP'
    obp_against_lhp_df['Subject'] = 'HitterId'
    obp_against_lhp_df['SubjectId'] = obp_against_lhp_df.index


    # Calculate slugging percentage against rhp 
    slg_against_rhp = ((raw_df[raw_df['PitcherSide']=='R'].groupby('HitterId')['TB'].sum()) \
    	/ (raw_df[raw_df['PitcherSide']=='R'].groupby('HitterId')['AB'].sum())).round(3)

    # Calculate slugging percentage against lhp 
    slg_against_lhp = ((raw_df[raw_df['PitcherSide']=='L'].groupby('HitterId')['TB'].sum()) \
    	/ (raw_df[raw_df['PitcherSide']=='L'].groupby('HitterId')['AB'].sum())).round(3)

    # Dataframes
    slg_against_rhp_df = slg_against_rhp.to_frame(name='Value')
    slg_against_rhp_df['Stat'] = 'SLG'
    slg_against_rhp_df['Split'] = 'vs RHP'
    slg_against_rhp_df['Subject'] = 'HitterId'
    slg_against_rhp_df['SubjectId'] = slg_against_rhp_df.index

    slg_against_lhp_df = slg_against_lhp.to_frame(name='Value')
    slg_against_lhp_df['Stat'] = 'SLG'
    slg_against_lhp_df['Split'] = 'vs LHP'
    slg_against_lhp_df['Subject'] = 'HitterId'
    slg_against_lhp_df['SubjectId'] = slg_against_lhp_df.index


    # Calculate OPS against righties
    ops_against_rhp = (obp_against_rhp + slg_against_rhp).round(3)

    # Now against lefties
    ops_against_lhp = (obp_against_lhp + slg_against_lhp).round(3)

    # Yay more dataframes 
    ops_against_rhp_df = ops_against_rhp.to_frame(name='Value')
    ops_against_rhp_df['Stat'] = 'OPS'
    ops_against_rhp_df['Split'] = 'vs RHP'
    ops_against_rhp_df['Subject'] = 'HitterId'
    ops_against_rhp_df['SubjectId'] = ops_against_rhp_df.index

    ops_against_lhp_df = ops_against_lhp.to_frame(name='Value')
    ops_against_lhp_df['Stat'] = 'OPS'
    ops_against_lhp_df['Split'] = 'vs LHP'
    ops_against_lhp_df['Subject'] = 'HitterId'
    ops_against_lhp_df['SubjectId'] = ops_against_lhp_df.index


    # # #
    # Team stats - Batting
    # # #

	# Now we can calculate a team's BA against righties
    team_avg_against_rhp = ((raw_df[raw_df['PitcherSide']=='R'].groupby('HitterTeamId')['H'].sum()) \
    	/ (raw_df[raw_df['PitcherSide']=='R'].groupby('HitterTeamId')['AB'].sum())).round(3)

    # And against southpaws
    team_avg_against_lhp = ((raw_df[raw_df['PitcherSide']=='L'].groupby('HitterTeamId')['H'].sum()) \
    	/ (raw_df[raw_df['PitcherSide']=='L'].groupby('HitterTeamId')['AB'].sum())).round(3)

    # Create dataframes
    team_avg_against_rhp_df = team_avg_against_rhp.to_frame(name='Value')
    team_avg_against_rhp_df['Stat'] = 'AVG'
    team_avg_against_rhp_df['Split'] = 'vs RHP'
    team_avg_against_rhp_df['Subject'] = 'HitterTeamId'
    team_avg_against_rhp_df['SubjectId'] = team_avg_against_rhp_df.index

    team_avg_against_lhp_df = team_avg_against_lhp.to_frame(name='Value')
    team_avg_against_lhp_df['Stat'] = 'AVG'
    team_avg_against_lhp_df['Split'] = 'vs LHP'
    team_avg_against_lhp_df['Subject'] = 'HitterTeamId'
    team_avg_against_lhp_df['SubjectId'] = team_avg_against_lhp_df.index


    # Do the wall again for team OBP
    team_obp_against_rhp = (((raw_df[raw_df['PitcherSide']=='R'].groupby('HitterTeamId')['H'].sum()) \
    	+ (raw_df[raw_df['PitcherSide']=='R'].groupby('HitterTeamId')['BB'].sum()) \
    	+ (raw_df[raw_df['PitcherSide']=='R'].groupby('HitterTeamId')['HBP'].sum())) \
    	/ ((raw_df[raw_df['PitcherSide']=='R'].groupby('HitterTeamId')['AB'].sum()) \
    	+ (raw_df[raw_df['PitcherSide']=='R'].groupby('HitterTeamId')['BB'].sum()) \
    	+ (raw_df[raw_df['PitcherSide']=='R'].groupby('HitterTeamId')['HBP'].sum()) \
    	+ (raw_df[raw_df['PitcherSide']=='R'].groupby('HitterTeamId')['SF'].sum()))).round(3)

    # Now for a team's OBP against lefties
    team_obp_against_lhp = (((raw_df[raw_df['PitcherSide']=='L'].groupby('HitterTeamId')['H'].sum()) \
    	+ (raw_df[raw_df['PitcherSide']=='L'].groupby('HitterTeamId')['BB'].sum()) \
    	+ (raw_df[raw_df['PitcherSide']=='L'].groupby('HitterTeamId')['HBP'].sum())) \
    	/ ((raw_df[raw_df['PitcherSide']=='L'].groupby('HitterTeamId')['AB'].sum()) \
    	+ (raw_df[raw_df['PitcherSide']=='L'].groupby('HitterTeamId')['BB'].sum()) \
    	+ (raw_df[raw_df['PitcherSide']=='L'].groupby('HitterTeamId')['HBP'].sum()) \
    	+ (raw_df[raw_df['PitcherSide']=='L'].groupby('HitterTeamId')['SF'].sum()))).round(3)

    # Dataframes
    team_obp_against_rhp_df = team_obp_against_rhp.to_frame(name='Value')
    team_obp_against_rhp_df['Stat'] = 'OBP'
    team_obp_against_rhp_df['Split'] = 'vs RHP'
    team_obp_against_rhp_df['Subject'] = 'HitterTeamId'
    team_obp_against_rhp_df['SubjectId'] = team_obp_against_rhp_df.index

    team_obp_against_lhp_df = team_obp_against_lhp.to_frame(name='Value')
    team_obp_against_lhp_df['Stat'] = 'OBP'
    team_obp_against_lhp_df['Split'] = 'vs LHP'
    team_obp_against_lhp_df['Subject'] = 'HitterTeamId'
    team_obp_against_lhp_df['SubjectId'] = team_obp_against_lhp_df.index


    # Calculate team slugging percentage against rhp 
    team_slg_against_rhp = ((raw_df[raw_df['PitcherSide']=='R'].groupby('HitterTeamId')['TB'].sum()) \
    	/ (raw_df[raw_df['PitcherSide']=='R'].groupby('HitterTeamId')['AB'].sum())).round(3)

    # Calculate team slugging percentage against lhp 
    team_slg_against_lhp = ((raw_df[raw_df['PitcherSide']=='L'].groupby('HitterTeamId')['TB'].sum()) \
    	/ (raw_df[raw_df['PitcherSide']=='L'].groupby('HitterTeamId')['AB'].sum())).round(3)

    # Team slugging dataframes
    team_slg_against_rhp_df = team_slg_against_rhp.to_frame(name='Value')
    team_slg_against_rhp_df['Stat'] = 'SLG'
    team_slg_against_rhp_df['Split'] = 'vs RHP'
    team_slg_against_rhp_df['Subject'] = 'HitterTeamId'
    team_slg_against_rhp_df['SubjectId'] = team_slg_against_rhp_df.index

    team_slg_against_lhp_df = team_slg_against_lhp.to_frame(name='Value')
    team_slg_against_lhp_df['Stat'] = 'SLG'
    team_slg_against_lhp_df['Split'] = 'vs LHP'
    team_slg_against_lhp_df['Subject'] = 'HitterTeamId'
    team_slg_against_lhp_df['SubjectId'] = team_slg_against_lhp_df.index


    # End with team ops
    team_ops_against_rhp = (team_obp_against_rhp + team_slg_against_rhp).round(3)

    # Now against lefties
    team_ops_against_lhp = (team_obp_against_lhp + team_slg_against_lhp).round(3)

    # last set of batting dfs
    team_ops_against_rhp_df = team_ops_against_rhp.to_frame(name='Value')
    team_ops_against_rhp_df['Stat'] = 'OPS'
    team_ops_against_rhp_df['Split'] = 'vs RHP'
    team_ops_against_rhp_df['Subject'] = 'HitterTeamId'
    team_ops_against_rhp_df['SubjectId'] = team_ops_against_rhp_df.index

    team_ops_against_lhp_df = team_ops_against_lhp.to_frame(name='Value')
    team_ops_against_lhp_df['Stat'] = 'OPS'
    team_ops_against_lhp_df['Split'] = 'vs LHP'
    team_ops_against_lhp_df['Subject'] = 'HitterTeamId'
    team_ops_against_lhp_df['SubjectId'] = team_ops_against_lhp_df.index


    # # #
    # Individual stats - Pitching
    # # # 

    # Let's look at a pitcher's BA against vs right handed hitters
    avg_against_rhh = ((raw_df[raw_df['HitterSide']=='R'].groupby('PitcherId')['H'].sum()) \
    	/ (raw_df[raw_df['HitterSide']=='R'].groupby('PitcherId')['AB'].sum())).round(3)

    # Now let's see pitching against lefties
    avg_against_lhh = ((raw_df[raw_df['HitterSide']=='L'].groupby('PitcherId')['H'].sum()) \
    	/ (raw_df[raw_df['HitterSide']=='L'].groupby('PitcherId')['AB'].sum())).round(3)

    # Generate first of the pitching dataframes
    avg_against_rhh_df = avg_against_rhh.to_frame(name='Value')
    avg_against_rhh_df['Stat'] = 'AVG'
    avg_against_rhh_df['Split'] = 'vs RHH'
    avg_against_rhh_df['Subject'] = 'PitcherId'
    avg_against_rhh_df['SubjectId'] = avg_against_rhh_df.index

    avg_against_lhh_df = avg_against_lhh.to_frame(name='Value')
    avg_against_lhh_df['Stat'] = 'AVG'
    avg_against_lhh_df['Split'] = 'vs LHH'
    avg_against_lhh_df['Subject'] = 'PitcherId'
    avg_against_lhh_df['SubjectId'] = avg_against_lhh_df.index


    # Find each pitcher's OBP against right handers
    obp_against_rhh = (((raw_df[raw_df['HitterSide']=='R'].groupby('PitcherId')['H'].sum()) \
    	+ (raw_df[raw_df['HitterSide']=='R'].groupby('PitcherId')['BB'].sum()) \
    	+ (raw_df[raw_df['HitterSide']=='R'].groupby('PitcherId')['HBP'].sum())) \
    	/ ((raw_df[raw_df['HitterSide']=='R'].groupby('PitcherId')['AB'].sum()) \
    	+ (raw_df[raw_df['HitterSide']=='R'].groupby('PitcherId')['BB'].sum()) \
    	+ (raw_df[raw_df['HitterSide']=='R'].groupby('PitcherId')['HBP'].sum()) \
    	+ (raw_df[raw_df['HitterSide']=='R'].groupby('PitcherId')['SF'].sum()))).round(3)

    # And for a pitcher's OBP against lefties
    obp_against_lhh = (((raw_df[raw_df['HitterSide']=='L'].groupby('PitcherId')['H'].sum()) \
    	+ (raw_df[raw_df['HitterSide']=='L'].groupby('PitcherId')['BB'].sum()) \
    	+ (raw_df[raw_df['HitterSide']=='L'].groupby('PitcherId')['HBP'].sum())) \
    	/ ((raw_df[raw_df['HitterSide']=='L'].groupby('PitcherId')['AB'].sum()) \
    	+ (raw_df[raw_df['HitterSide']=='L'].groupby('PitcherId')['BB'].sum()) \
    	+ (raw_df[raw_df['HitterSide']=='L'].groupby('PitcherId')['HBP'].sum()) \
    	+ (raw_df[raw_df['HitterSide']=='L'].groupby('PitcherId')['SF'].sum()))).round(3)

    # Dataframes for obp against
    obp_against_rhh_df = obp_against_rhh.to_frame(name='Value')
    obp_against_rhh_df['Stat'] = 'OBP'
    obp_against_rhh_df['Split'] = 'vs RHH'
    obp_against_rhh_df['Subject'] = 'PitcherId'
    obp_against_rhh_df['SubjectId'] = obp_against_rhh_df.index

    obp_against_lhh_df = obp_against_lhh.to_frame(name='Value')
    obp_against_lhh_df['Stat'] = 'OBP'
    obp_against_lhh_df['Split'] = 'vs LHH'
    obp_against_lhh_df['Subject'] = 'PitcherId'
    obp_against_lhh_df['SubjectId'] = obp_against_lhh_df.index
    

    # How about slugging percentage against rhh 
    slg_against_rhh = ((raw_df[raw_df['HitterSide']=='R'].groupby('PitcherId')['TB'].sum()) \
    	/ (raw_df[raw_df['HitterSide']=='R'].groupby('PitcherId')['AB'].sum())).round(3)

    # Then slugging percentage against lhh 
    slg_against_lhh = ((raw_df[raw_df['HitterSide']=='L'].groupby('PitcherId')['TB'].sum()) \
    	/ (raw_df[raw_df['HitterSide']=='L'].groupby('PitcherId')['AB'].sum())).round(3)

    # Dataframes
    slg_against_rhh_df = slg_against_rhh.to_frame(name='Value')
    slg_against_rhh_df['Stat'] = 'SLG'
    slg_against_rhh_df['Split'] = 'vs RHH'
    slg_against_rhh_df['Subject'] = 'PitcherId'
    slg_against_rhh_df['SubjectId'] = slg_against_rhh_df.index

    slg_against_lhh_df = slg_against_lhh.to_frame(name='Value')
    slg_against_lhh_df['Stat'] = 'SLG'
    slg_against_lhh_df['Split'] = 'vs LHH'
    slg_against_lhh_df['Subject'] = 'PitcherId'
    slg_against_lhh_df['SubjectId'] = slg_against_lhh_df.index


    # Calculate OPS against for right handed batters
    ops_against_rhh = (obp_against_rhh + slg_against_rhh).round(3)

    # Now against lefties
    ops_against_lhh = (obp_against_lhh + slg_against_lhh).round(3)
    # Whoever 656546 is has some really solid stuff 
    # last dataframes
    ops_against_rhh_df = ops_against_rhh.to_frame(name='Value')
    ops_against_rhh_df['Stat'] = 'OPS'
    ops_against_rhh_df['Split'] = 'vs RHH'
    ops_against_rhh_df['Subject'] = 'PitcherId'
    ops_against_rhh_df['SubjectId'] = ops_against_rhh_df.index

    ops_against_lhh_df = ops_against_lhh.to_frame(name='Value')
    ops_against_lhh_df['Stat'] = 'OPS'
    ops_against_lhh_df['Split'] = 'vs LHH'
    ops_against_lhh_df['Subject'] = 'PitcherId'
    ops_against_lhh_df['SubjectId'] = ops_against_lhh_df.index


    # # #
    # Team stats - Pitching
    # # #

	# Now we can calculate a pitching staff's BA against for righties
    team_avg_against_rhh = ((raw_df[raw_df['HitterSide']=='R'].groupby('PitcherTeamId')['H'].sum()) \
    	/ (raw_df[raw_df['HitterSide']=='R'].groupby('PitcherTeamId')['AB'].sum())).round(3)

    # Against lefties
    team_avg_against_lhh = ((raw_df[raw_df['HitterSide']=='L'].groupby('PitcherTeamId')['H'].sum()) \
    	/ (raw_df[raw_df['HitterSide']=='L'].groupby('PitcherTeamId')['AB'].sum())).round(3)

    # Last set of data frames
    team_avg_against_rhh_df = team_avg_against_rhh.to_frame(name='Value')
    team_avg_against_rhh_df['Stat'] = 'AVG'
    team_avg_against_rhh_df['Split'] = 'vs RHH'
    team_avg_against_rhh_df['Subject'] = 'PitcherTeamId'
    team_avg_against_rhh_df['SubjectId'] = team_avg_against_rhh_df.index

    team_avg_against_lhh_df = team_avg_against_lhh.to_frame(name='Value')
    team_avg_against_lhh_df['Stat'] = 'AVG'
    team_avg_against_lhh_df['Split'] = 'vs LHH'
    team_avg_against_lhh_df['Subject'] = 'PitcherTeamId'
    team_avg_against_lhh_df['SubjectId'] = team_avg_against_lhh_df.index


    # Do the wall one last time for team OBP against
    team_obp_against_rhh = (((raw_df[raw_df['HitterSide']=='R'].groupby('PitcherTeamId')['H'].sum()) \
    	+ (raw_df[raw_df['HitterSide']=='R'].groupby('PitcherTeamId')['BB'].sum()) \
    	+ (raw_df[raw_df['HitterSide']=='R'].groupby('PitcherTeamId')['HBP'].sum())) \
    	/ ((raw_df[raw_df['HitterSide']=='R'].groupby('PitcherTeamId')['AB'].sum()) \
    	+ (raw_df[raw_df['HitterSide']=='R'].groupby('PitcherTeamId')['BB'].sum()) \
    	+ (raw_df[raw_df['HitterSide']=='R'].groupby('PitcherTeamId')['HBP'].sum()) \
    	+ (raw_df[raw_df['HitterSide']=='R'].groupby('PitcherTeamId')['SF'].sum()))).round(3)

    team_obp_against_lhh = (((raw_df[raw_df['HitterSide']=='L'].groupby('PitcherTeamId')['H'].sum()) \
    	+ (raw_df[raw_df['HitterSide']=='L'].groupby('PitcherTeamId')['BB'].sum()) \
    	+ (raw_df[raw_df['HitterSide']=='L'].groupby('PitcherTeamId')['HBP'].sum())) \
    	/ ((raw_df[raw_df['HitterSide']=='L'].groupby('PitcherTeamId')['AB'].sum()) \
    	+ (raw_df[raw_df['HitterSide']=='L'].groupby('PitcherTeamId')['BB'].sum()) \
    	+ (raw_df[raw_df['HitterSide']=='L'].groupby('PitcherTeamId')['HBP'].sum()) \
    	+ (raw_df[raw_df['HitterSide']=='L'].groupby('PitcherTeamId')['SF'].sum()))).round(3)

    # Dataframes
    team_obp_against_rhh_df = team_obp_against_rhh.to_frame(name='Value')
    team_obp_against_rhh_df['Stat'] = 'OBP'
    team_obp_against_rhh_df['Split'] = 'vs RHH'
    team_obp_against_rhh_df['Subject'] = 'PitcherTeamId'
    team_obp_against_rhh_df['SubjectId'] = team_obp_against_rhh_df.index

    team_obp_against_lhh_df = team_obp_against_lhh.to_frame(name='Value')
    team_obp_against_lhh_df['Stat'] = 'OBP'
    team_obp_against_lhh_df['Split'] = 'vs LHH'
    team_obp_against_lhh_df['Subject'] = 'PitcherTeamId'
    team_obp_against_lhh_df['SubjectId'] = team_obp_against_lhh_df.index


    # Calculate team slugging percentage vs rhh
    team_slg_against_rhh = ((raw_df[raw_df['HitterSide']=='R'].groupby('PitcherTeamId')['TB'].sum()) \
    	/ (raw_df[raw_df['HitterSide']=='R'].groupby('PitcherTeamId')['AB'].sum())).round(3)

    # Finally end with team slugging percentage against vs lhh 
    team_slg_against_lhh = ((raw_df[raw_df['HitterSide']=='L'].groupby('PitcherTeamId')['TB'].sum()) \
    	/ (raw_df[raw_df['HitterSide']=='L'].groupby('PitcherTeamId')['AB'].sum())).round(3)

    # I think you know these are the dataframes by now
    team_slg_against_rhh_df = team_slg_against_rhh.to_frame(name='Value')
    team_slg_against_rhh_df['Stat'] = 'SLG'
    team_slg_against_rhh_df['Split'] = 'vs RHH'
    team_slg_against_rhh_df['Subject'] = 'PitcherTeamId'
    team_slg_against_rhh_df['SubjectId'] = team_slg_against_rhh_df.index

    team_slg_against_lhh_df = team_slg_against_lhh.to_frame(name='Value')
    team_slg_against_lhh_df['Stat'] = 'SLG'
    team_slg_against_lhh_df['Split'] = 'vs LHH'
    team_slg_against_lhh_df['Subject'] = 'PitcherTeamId'
    team_slg_against_lhh_df['SubjectId'] = team_slg_against_lhh_df.index


    # End with team ops
    team_ops_against_rhh = (team_obp_against_rhh + team_slg_against_rhh).round(3)

    # Now against lefties
    team_ops_against_lhh = (team_obp_against_lhh + team_slg_against_lhh).round(3)

    # Final set of individual dataframes
    team_ops_against_rhh_df = team_ops_against_rhh.to_frame(name='Value')
    team_ops_against_rhh_df['Stat'] = 'OPS'
    team_ops_against_rhh_df['Split'] = 'vs RHH'
    team_ops_against_rhh_df['Subject'] = 'PitcherTeamId'
    team_ops_against_rhh_df['SubjectId'] = team_ops_against_rhh_df.index

    team_ops_against_lhh_df = team_ops_against_lhh.to_frame(name='Value')
    team_ops_against_lhh_df['Stat'] = 'OPS'
    team_ops_against_lhh_df['Split'] = 'vs LHH'
    team_ops_against_lhh_df['Subject'] = 'PitcherTeamId'
    team_ops_against_lhh_df['SubjectId'] = team_ops_against_lhh_df.index


    # # # # # # # # # # # # # # # # #
    # Filter out low at-bat records #
    # # # # # # # # # # # # # # # # #

    # Begin by calculating who has and hasn't hit 25 at bats (or at bats against) each opportunity
    pa_against_rhp = raw_df[raw_df['PitcherSide']=='R'].groupby('HitterId')['PA'].sum() >= 25
    pa_against_lhp = raw_df[raw_df['PitcherSide']=='L'].groupby('HitterId')['PA'].sum() >= 25
    team_pa_against_rhp = raw_df[raw_df['PitcherSide']=='R'].groupby('HitterTeamId')['PA'].sum() >= 25
    team_pa_against_lhp = raw_df[raw_df['PitcherSide']=='L'].groupby('HitterTeamId')['PA'].sum() >= 25
    pa_against_rhh = raw_df[raw_df['HitterSide']=='R'].groupby('PitcherId')['PA'].sum() >= 25
    pa_against_lhh = raw_df[raw_df['HitterSide']=='L'].groupby('PitcherId')['PA'].sum() >= 25
    team_pa_against_rhh = raw_df[raw_df['HitterSide']=='R'].groupby('PitcherTeamId')['PA'].sum() >= 25
    team_pa_against_lhh = raw_df[raw_df['HitterSide']=='L'].groupby('PitcherTeamId')['PA'].sum() >= 25
	#print(team_pa_against_lhp)

    # Create our dataframes of booleans - True if PA > 25
    # Note - I'm purposely not going to do team AB counts, all teams pass 25 ABs for all 4 options
    pa_against_rhp_df = pa_against_rhp.to_frame(name = "ABCount") 
    pa_against_rhp_df['SubjectId'] = pa_against_rhp_df.index

    pa_against_lhp_df = pa_against_lhp.to_frame(name = "ABCount") 
    pa_against_lhp_df['SubjectId'] = pa_against_lhp_df.index

    pa_against_rhh_df = pa_against_rhh.to_frame(name = "ABCount") 
    pa_against_rhh_df['SubjectId'] = pa_against_rhh_df.index

    pa_against_lhh_df = pa_against_lhh.to_frame(name = "ABCount") 
    pa_against_lhh_df['SubjectId'] = pa_against_lhh_df.index

    # Now we can merge the bool table with the stats table,
    # From this we can remove any False records - those with <25 ABs
    merged_avg_against_rhp = pandas.merge(avg_against_rhp_df, pa_against_rhp_df)
    merged_avg_against_rhp = merged_avg_against_rhp[merged_avg_against_rhp.ABCount]
    merged_avg_against_lhp = pandas.merge(avg_against_lhp_df, pa_against_lhp_df)
    merged_avg_against_lhp = merged_avg_against_lhp[merged_avg_against_lhp.ABCount]

    merged_obp_against_rhp = pandas.merge(obp_against_rhp_df, pa_against_rhp_df)
    merged_obp_against_rhp = merged_obp_against_rhp[merged_obp_against_rhp.ABCount]
    merged_obp_against_lhp = pandas.merge(obp_against_lhp_df, pa_against_lhp_df)
    merged_obp_against_lhp = merged_obp_against_lhp[merged_obp_against_lhp.ABCount]

    merged_slg_against_rhp = pandas.merge(slg_against_rhp_df, pa_against_rhp_df)
    merged_slg_against_rhp = merged_slg_against_rhp[merged_slg_against_rhp.ABCount]
    merged_slg_against_lhp = pandas.merge(slg_against_lhp_df, pa_against_lhp_df)
    merged_slg_against_lhp = merged_slg_against_lhp[merged_slg_against_lhp.ABCount]

    merged_ops_against_rhp = pandas.merge(ops_against_rhp_df, pa_against_rhp_df)
    merged_ops_against_rhp = merged_ops_against_rhp[merged_ops_against_rhp.ABCount]
    merged_ops_against_lhp = pandas.merge(ops_against_lhp_df, pa_against_lhp_df)
    merged_ops_against_lhp = merged_ops_against_lhp[merged_ops_against_lhp.ABCount]

    merged_avg_against_rhh = pandas.merge(avg_against_rhh_df, pa_against_rhh_df)
    merged_avg_against_rhh = merged_avg_against_rhh[merged_avg_against_rhh.ABCount]
    merged_avg_against_lhh = pandas.merge(avg_against_lhh_df, pa_against_lhh_df)
    merged_avg_against_lhh = merged_avg_against_lhh[merged_avg_against_lhh.ABCount]

    merged_obp_against_rhh = pandas.merge(obp_against_rhh_df, pa_against_rhh_df)
    merged_obp_against_rhh = merged_obp_against_rhh[merged_obp_against_rhh.ABCount]
    merged_obp_against_lhh = pandas.merge(obp_against_lhh_df, pa_against_lhh_df)
    merged_obp_against_lhh = merged_obp_against_lhh[merged_obp_against_lhh.ABCount]

    merged_slg_against_rhh = pandas.merge(slg_against_rhh_df, pa_against_rhh_df)
    merged_slg_against_rhh = merged_slg_against_rhh[merged_slg_against_rhh.ABCount]
    merged_slg_against_lhh = pandas.merge(slg_against_lhh_df, pa_against_lhh_df)
    merged_slg_against_lhh = merged_slg_against_lhh[merged_slg_against_lhh.ABCount]
   
    merged_ops_against_rhh = pandas.merge(ops_against_rhh_df, pa_against_rhh_df)
    merged_ops_against_rhh = merged_ops_against_rhh[merged_ops_against_rhh.ABCount]
    merged_ops_against_lhh = pandas.merge(ops_against_lhh_df, pa_against_lhh_df)
    merged_ops_against_lhh = merged_ops_against_lhh[merged_ops_against_lhh.ABCount]
    #print(merged_avg_against_lhh)


    # # # # # # # # # # # # # # 
    # Aggregate our subtables #
    # # # # # # # # # # # # # #

    # We can now combine our subtables to be sorted and exported
    aggregate_df = merged_avg_against_rhp.append([merged_avg_against_lhp, \
    	merged_obp_against_rhp, merged_obp_against_lhp, \
    	merged_slg_against_rhp, merged_slg_against_lhp, \
    	merged_ops_against_rhp, merged_ops_against_lhp, \
    	team_avg_against_rhp_df, team_avg_against_lhp_df, \
    	team_obp_against_rhp_df, team_obp_against_lhp_df, \
    	team_slg_against_rhp_df, team_slg_against_lhp_df, \
    	team_ops_against_rhp_df, team_ops_against_lhp_df, \
    	merged_avg_against_rhh, merged_avg_against_lhh, \
    	merged_obp_against_rhh, merged_obp_against_lhh, \
    	merged_slg_against_rhh, merged_slg_against_lhh, \
    	merged_ops_against_rhh, merged_ops_against_lhh, \
    	team_avg_against_rhh_df, team_avg_against_lhh_df,\
    	team_obp_against_rhh_df, team_obp_against_lhh_df, \
    	team_slg_against_rhh_df, team_slg_against_lhh_df, \
    	team_ops_against_rhh_df, team_ops_against_lhh_df])

    # Reorganize the order of the columns
    aggregate_df = aggregate_df[['SubjectId', 'Stat', 'Split', 'Subject', 'Value']]

    # Now sort over first four columns
    sorted_aggregate_df = aggregate_df.sort_values(by=['SubjectId','Stat','Split','Subject'])

    # Finally write the aggregated table to a csv 
    sorted_aggregate_df.to_csv('./data/processed/output.csv', encoding='utf-8', index=False)

    # We did it! Go Twins 
    pass


if __name__ == '__main__':
    main()
