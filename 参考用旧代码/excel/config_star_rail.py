from collections import namedtuple
from enum import IntEnum
from .util import *
_text_map = None


class _TextID:
	_no_tran_msg_fmt = "TextID(%d)"
	def __init__(self, hash_sum):
		self._hash_sum = hash_sum

	def __str__(self):
		content = self.get_content()[0]
		if content:
			return content
		return self._no_tran_msg_fmt%self._hash_sum

	def get_content(self):
		content = (None, False)
		if _text_map:
			content = _text_map._get(self._hash_sum)
		return content

	def __repr__(self):
		content = self.get_content()[0]
		if content:
			return content.__repr__()
		return self._no_tran_msg_fmt%self._hash_sum


class SRTrans:
	def __init__(self, data):
		from .parser import decode_excel
		self.text_map = {}
		for hash_sum, content, has_param in decode_excel(*TextMap, data):
			self.text_map[hash_sum] = (content.replace(r'\n', '\n'), has_param)

	def __getitem__(self, item):
		if isinstance(item, dict):
			return self.text_map.get(item['hash'], ('', False))[0]
		return item

	def _get(self, item):
		return self.text_map.get(item, (None, False))

	def get(self, item):
		return self.__getitem__(item)


TextID = (_TextID, ((0, (True,), None),))
TextMap = (namedtuple('TextMap', ('id', 'text', 'has_param')), ((0, (True,), None), (1, (), None), (0, (), (bool,()))))


# ——————Generated Code——————
class MissionBeginType(IntEnum):
	Unknown = 0
	Auto = 1
	Manual = 2
	Client = 3
	MultiSequence = 4
	PlayerLevel = 5
	WorldLevel = 6
	MultiEvent = 7
	HeroPathLevel = 9
	SequenceNextDay = 10
	CustomValue = 11
	AnySequence = 12
	MuseumPhaseRenewPointReach = 13
	HeliobusPhaseReach = 14


class ModifierBehaviorFlag(IntEnum):
	Unknow = 0
	RemoveWhenCasterDead = 1
	DisableAction = 2
	OneMore = 3
	Taunt = 4
	BurstBP = 5
	Break = 6
	LifeStepImmediately = 7
	IdleNormalDebuff = 8
	IdleStun = 9
	Shield = 10
	DisableHealHP = 11
	Endurance = 12
	EnduranceEnemyOnly = 13
	Stealth = 14
	BlockDamage = 15
	BlockDamageExcludeDot = 16
	Dodge = 17
	MuteHitFly = 18
	MuteHitH = 19
	MuteBreak = 20
	Deathrattle = 21
	BloodLink = 22
	Revivable = 23
	AvatarBreak = 24
	ResistDebuff = 25
	TeamAction = 26
	AttackSign = 27
	Crazy = 28
	ForceStanceDamage = 29
	OffTeamFormation = 30
	RemoveWhenOwnerUnstage = 31
	RemoveWhenCasterUnstage = 32
	DispelPriorityHigh = 33
	MuteAttachWeakness = 34
	Charm = 35
	StoreDamage = 36
	BreakExtend = 37
	AITargetLowerPriority = 38
	KeepOnDeathrattle = 39
	ModifyDotDamageData = 40
	ModifyDotHealData = 41
	RedStance = 42
	IgnoreSPCheck = 43
	TauntForAutoLock = 44
	MuteSpeed = 45
	ListenUnStage = 46
	Bakcup = 47
	Bakcup2 = 48
	Bakcup3 = 49
	Bakcup4 = 50
	FixedPerformTime = 51
	UnOperable = 52
	ListenBattleEventSkill = 53
	AlwaysSuccess = 54
	STAT_DefenceDown = 100
	STAT_Fatigue = 101
	STAT_SpeedDown = 102
	STAT_DOT_Bleed = 103
	STAT_DOT_Burn = 104
	STAT_CTRL = 105
	STAT_CTRL_Stun = 106
	STAT_CTRL_Frozen = 107
	STAT_DOT_Poison = 108
	STAT_DOT = 109
	STAT_DOT_Electric = 110
	STAT_Confine = 111
	STAT_Burst = 112
	STAT_SpeedUp = 113
	STAT_CTRL_Frozen_Effect = 114
	STAT_CTRL_Sleep = 115
	STAT_AttachWeakness = 116
	STAT_AnimStop = 118
	STAT_Entangle = 119
	STAT_AttackDown = 120
	STAT_CTRL_Shake = 121
	STAT_CTRL_UnOperable = 122
	CustomEvent_InfiniteRefresh = 1000
	CustomEvent_MonsterChangePhase = 1001


class AttackDamageType(IntEnum):
	Unknow = 0
	Physical = 1
	Fire = 2
	Ice = 4
	Thunder = 8
	Wind = 16
	Quantum = 32
	Imaginary = 64
	Heal = 128
	AllType = 255


PlaneType = IntEnum('PlaneType', ('Unknown', 'Town', 'Maze', 'Train', 'Challenge', 'Rogue', 'Raid', 'AetherDivide', 'TrialActivity'), start=0)
FloorType = IntEnum('FloorType', ('Unknown', 'Default', 'Indoor'), start=0)
StageType = IntEnum('StageType', ('Unknown', 'Mainline', 'Maze', 'Adventure', 'Cocoon', 'FarmElement', 'Client', 'FarmRelic', 'VerseSimulation', 'Trial', 'PunkLord', 'FightActivity', 'TrialAdventure', 'BoxingClub', 'TrialInBattle', 'RogueChallengeActivity', 'TreasureDungeon', 'AetherDivide', 'FantasticStory', 'BattleCollege', 'Heliobus', 'RogueEndlessActivity'), start=0)
RhythmType = IntEnum('RhythmType', ('TYPE_TENSE', 'TYPE_EASY'), start=0)
FarmTypeConfig = IntEnum('FarmTypeConfig', ('NONE', 'COCOON', 'COCOON2', 'ELEMENT', 'RELIC', 'COCOON3'), start=0)
MappingInfoType = IntEnum('MappingInfoType', ('NONE', 'CHALLENGE_ENTRANCE', 'ROGUE_ENTRANCE', 'RAID_ENTRANCE', 'WORLD_SHOP_ENTRANCE', 'ACTIVITY_ENTRANCE', 'FARM_ENTRANCE', 'HELIOBUS_CHALLENGE', 'HELIOBUS_RAID', 'DRONE_ENTRANCE'), start=0)
MapEntryType = IntEnum('MapEntryType', ('Unknown', 'Town', 'Mission', 'Explore'), start=0)
LogicOperation = IntEnum('LogicOperation', ('None', 'Or', 'And'), start=0)
MainMissionType = IntEnum('MainMissionType', ('None', 'Main', 'Branch', 'Daily', 'Rogue', 'Raid', 'Companion', 'Gap'), start=0)
ConditionType = IntEnum('ConditionType', ('None', 'FinishMainMission', 'PlayerLevel', 'WorldLevel', 'FinishChallenge', 'NotInPlaneType', 'AvatarLevel', 'FinishSubMission', 'FinishQuest', 'MaxPlayerLevel', 'QuestClose', 'CanUseFoodInRogue'), start=0)
MazeBuffInBattleBindingType = IntEnum('MazeBuffInBattleBindingType', ('None', 'StageAbility', 'CharacterSkill', 'CharacterAbility', 'StageAbilityBeforeCharacterBorn', 'StageAbilityAfterCharacterBorn'), start=0)
MazeBuffType = IntEnum('MazeBuffType', ('None', 'Character', 'Team', 'Level', 'CharacterKeepScene', 'TeamKeepScene', 'LevelKeepScene'), start=0)
MazeBuffUseType = IntEnum('MazeBuffUseType', ('None', 'TriggerBattle', 'AddBattleBuff', 'SummonUnit', 'Special'), start=0)
EnumStatusType = IntEnum('EnumStatusType', ('Unknown', 'Buff', 'Debuff', 'Other'), start=0)
NAIPLOCEJIC = (namedtuple('NAIPLOCEJIC', ('lfciilhabdo', 'bjalgpncikp', 'ajihcmffaob', 'ggdmegbgeli', 'ahjbjidmadg', 'laleeadfofa', 'mmcfljjbkjk')), ((1, (), None), (1, (), None), (1, (), None), (1, (), None), (1, (), None), (1, (), None), (1, (), None)))
EPFLFIEAKLN = (namedtuple('EPFLFIEAKLN', ('name', 'value')), ((1, (), None), (1, (), None)))
StageMonsterWave = (namedtuple('StageMonsterWave', ('monster0', 'monster1', 'monster2', 'monster3', 'monster4')), ((0, (), None), (0, (), None), (0, (), None), (0, (), None), (0, (), None)))
ItemConfig = (namedtuple('ItemConfig', ('item_id', 'item_num')), ((0, (), None), (0, (), None)))
MissionCondition = (namedtuple('MissionCondition', ('type', 'value')), ((0, (True,), (MissionBeginType,())), (0, (), None)))
CDCCIKAONNI = (namedtuple('CDCCIKAONNI', ('cfnmggclfhn', 'jcfbpdlnmlh')), ((1, (), None), (0, (True,), None)))
HMBBDJOMIOI = (namedtuple('HMBBDJOMIOI', ('cfnmggclfhn', 'jcfbpdlnmlh')), ((1, (), None), (0, (), (c,()))))
MonsterResistEntry = (namedtuple('MonsterResistEntry', ('key', 'value')), ((0, (True,), (ModifierBehaviorFlag,())), (0, (), (c,()))))
ElementResistanceConfig = (namedtuple('ElementResistanceConfig', ('damage_type', 'value')), ((0, (True,), (AttackDamageType,())), (0, (), (c,()))))
EMBOJMALLBE = (namedtuple('EMBOJMALLBE', ('obbncdoakef', 'mpifgobelol', 'ldijcomgdgi', 'ofhjiailnfb', 'kgdnleiainm', 'jebebbjjhhb', 'fccdobgopig', 'phjokdndgeg')), ((0, (), None), (0, (), None), (0, (), None), (0, (), None), (0, (), None), (0, (), None), (0, (), None), (0, (), None)))
ConditionParam = (namedtuple('ConditionParam', ('type', 'param')), ((0, (True,), (ConditionType,())), (1, (), None)))
VideoConfig = (namedtuple('VideoConfig', ('video_id', 'video_path', 'is_player_involved', 'caption_path', 'encryption')), ((0, (), None), (1, (), None), (0, (), (bool,())), (1, (), None), (0, (), (bool,()))))
BackGroundMusicGroup = (namedtuple('BackGroundMusicGroup', ('id', 'group_name', 'group_icon')), ((0, (), None), (3,TextID,None), (1, (), None)))
BackGroundMusic = (namedtuple('BackGroundMusic', ('id', 'group_id', 'music_name', 'unlock_desc', 'bgm_desc', 'music_switch_name', 'bpm', 'rhythm_colour', 'unlock')), ((0, (), None), (0, (), None), (3,TextID,None), (3,TextID,None), (3,TextID,None), (1, (), None), (0, (), None), (0, (True,), (RhythmType,())), (0, (), (bool,()))))
MazeFloor = (namedtuple('MazeFloor', ('floor_id', 'floor_name', 'base_floor_id', 'bgm_world_state', 'floor_bgm_group_name', 'floor_bgm_normal_state_name', 'floor_default_emotion', 'floor_bgm_busy_state_name', 'enter_audio_event', 'exit_audio_event', 'floor_type', 'walking_effect_additive_scale', 'optional_load_blocks_config', 'municipal_config_path', 'map_layer_name_list', 'combat_bgm_low', 'combat_bgm_high')), ((0, (), None), (1, (), None), (0, (), None), (1, (), None), (1, (), None), (1, (), None), (1, (), None), (1, (), None), (2, ((1, (), None),), None), (2, ((1, (), None),), None), (0, (True,), (FloorType,())), (5, (4,), (a,())), (1, (), None), (1, (), None), (2, ((3,TextID,None),), None), (1, (), None), (1, (), None)))
CutSceneConfig = (namedtuple('CutSceneConfig', ('cut_scene_name', 'is_player_involved', 'cut_scene_path', 'cut_scene_sfx_json_path', 'sfxid', 'voice_id', 'cut_scene_bgm_state_name', 'caption_path', 'pos_off_set', 'maze_plane_id', 'maze_floor_id', 'hide_block_list')), ((1, (), None), (0, (), (bool,())), (1, (), None), (1, (), None), (0, (), None), (0, (), None), (1, (), None), (1, (), None), (2, ((5, (4,), (a,())),), None), (0, (), None), (0, (), None), (2, ((1, (), None),), None)))
StageConfig = (namedtuple('StageConfig', ('stage_id', 'stage_type', 'stage_name', 'hard_level_group', 'level', 'elite_group', 'level_graph_path', 'stage_ability_config', 'battle_scoring_group', 'sub_level_graphs', 'stage_config_data', 'monster_list', 'level_lose_condition', 'level_win_condition', 'forbid_auto_battle', 'release', 'forbid_exit_battle', 'monster_warning_ratio', 'reset_battle_speed', 'trial_avatar_list')), ((0, (), None), (0, (True,), (StageType,())), (3,TextID,None), (0, (), None), (0, (), None), (0, (), None), (1, (), None), (2, ((1, (), None),), None), (0, (), None), (2, ((4,NAIPLOCEJIC,None),), None), (2, ((4,EPFLFIEAKLN,None),), None), (2, ((4,StageMonsterWave,None),), None), (2, ((1, (), None),), None), (2, ((1, (), None),), None), (0, (), (bool,())), (0, (), (bool,())), (0, (), (bool,())), (5, (4,), (a,())), (0, (), (bool,())), (2, ((0, (), None),), None)))
MazePlane = (namedtuple('MazePlane', ('plane_id', 'plane_type', 'sub_type', 'maze_pool_type', 'world_id', 'plane_name', 'start_floor_id', 'floor_id_list')), ((0, (), None), (0, (True,), (PlaneType,())), (0, (), None), (0, (), None), (0, (), None), (3,TextID,None), (0, (), None), (2, ((0, (), None),), None)))
MappingInfo = (namedtuple('MappingInfo', ('id', 'world_level', 'type', 'farm_type', 'is_teleport', 'is_show_in_fog', 'plane_id', 'floor_id', 'group_id', 'config_id', 'initial_enable', 'name', 'desc', 'show_monster_list', 'display_item_list', 'is_show_cleared', 'entrance_id')), ((0, (), None), (0, (), None), (0, (True,), (MappingInfoType,())), (0, (True,), (FarmTypeConfig,())), (0, (), (bool,())), (0, (), (bool,())), (0, (), None), (0, (), None), (0, (), None), (0, (), None), (0, (), (bool,())), (3,TextID,None), (3,TextID,None), (2, ((0, (), None),), None), (2, ((4,ItemConfig,None),), None), (0, (), (bool,())), (0, (), None)))
MapEntrance = (namedtuple('MapEntrance', ('id', 'entrance_type', 'plane_id', 'floor_id', 'start_group_id', 'start_anchor_id', 'begin_main_mission_list', 'finish_main_mission_list', 'finish_sub_mission_list')), ((0, (), None), (0, (True,), (MapEntryType,())), (0, (), None), (0, (), None), (0, (), None), (0, (), None), (2, ((0, (), None),), None), (2, ((0, (), None),), None), (2, ((0, (), None),), None)))
MapEntranceGroup = (namedtuple('MapEntranceGroup', ('id', 'map_guide_id', 'type', 'group_name')), ((0, (), None), (0, (), None), (0, (), None), (3,TextID,None)))
MapGuide = (namedtuple('MapGuide', ('id', 'world_id', 'map_guide_name', 'sheet_id', 'sheet_type', 'map_guide_icon_path')), ((0, (), None), (0, (), None), (3,TextID,None), (0, (), None), (0, (), None), (1, (), None)))
AreaMapConfig = (namedtuple('AreaMapConfig', ('id', 'name', 'menu_sort_id', 'menu_icon_id', 'from_area_map_id', 'from_mapping_info_id', 'is_unlock_after_enter')), ((0, (), None), (3,TextID,None), (0, (), None), (0, (), None), (0, (), None), (0, (), None), (0, (), (bool,()))))
MainMission = (namedtuple('MainMission', ('main_mission_id', 'type', 'display_priority', 'is_in_raid', 'next_main_mission_list', 'name', 'take_operation', 'begin_operation', 'take_param', 'begin_param', 'next_track_main_mission', 'track_weight', 'mission_suspend', 'mission_advance', 'reward_id', 'display_reward_id', 'chapter_id', 'sub_reward_list')), ((0, (), None), (0, (True,), (MainMissionType,())), (0, (), None), (0, (), (bool,())), (2, ((0, (), None),), None), (3,TextID,None), (0, (True,), (LogicOperation,())), (0, (True,), (LogicOperation,())), (2, ((4,MissionCondition,None),), None), (2, ((4,MissionCondition,None),), None), (0, (), None), (0, (), None), (0, (), None), (0, (), None), (0, (), None), (0, (), None), (0, (), None), (2, ((0, (), None),), None)))
MainMissionSchedule = (namedtuple('MainMissionSchedule', ('main_mission_id', 'schedule_data_id', 'hide_remain_time', 'activity_module_id')), ((0, (), None), (0, (), None), (0, (), (bool,())), (0, (), None)))
MonsterConfig = (namedtuple('MonsterConfig', ('monster_id', 'monster_template_id', 'monster_name', 'monster_introduction', 'monster_battle_introduction', 'monster_type', 'level', 'hard_level_group', 'elite_group', 'attack_modify_ratio', 'defence_modify_ratio', 'hp_modify_ratio', 'speed_modify_ratio', 'stance_modify_ratio', 'attack_modify_value', 'defence_modify_value', 'hp_modify_value', 'speed_modify_value', 'stance_modify_value', 'skill_list', 'custom_values', 'dynamic_values', 'debuff_resist', 'stance_count_delta', 'custom_value_tags', 'stance_weak_list', 'damage_type_resistance', 'ability_name_list', 'release', 'override_ai_path', 'override_ai_skill_sequence')), ((0, (), None), (0, (), None), (3,TextID,None), (3,TextID,None), (3,TextID,None), (0, (), None), (0, (), None), (0, (), None), (0, (), None), (0, (), (c,())), (0, (), (c,())), (0, (), (c,())), (0, (), (c,())), (0, (), (c,())), (0, (), (c,())), (0, (), (c,())), (0, (), (c,())), (0, (), (c,())), (0, (), (c,())), (2, ((0, (), None),), None), (2, ((4,CDCCIKAONNI,None),), None), (2, ((4,HMBBDJOMIOI,None),), None), (2, ((4,MonsterResistEntry,None),), None), (0, (True,), None), (2, ((1, (), None),), None), (2, ((0, (True,), (AttackDamageType,())),), None), (2, ((4,ElementResistanceConfig,None),), None), (2, ((1, (), None),), None), (0, (), (bool,())), (1, (), None), (2, ((4,EMBOJMALLBE,None),), None)))
WorldConfig = (namedtuple('WorldConfig', ('id', 'is_real_world', 'is_show', 'world_name', 'world_desc', 'dynamic_optional_block')), ((0, (), None), (0, (), (bool,())), (0, (), (bool,())), (3,TextID,None), (3,TextID,None), (1, (), None)))
ActivityPanel = (namedtuple('ActivityPanel', ('panel_id', 'type', 'activity_module_id', 'ui_prefab', 'type_param', 'unlock_conditions', 'hide_quest', 'sort_weight', 'tab_name', 'title_name', 'panel_desc', 'tab_icon', 'tag_desc', 'intro_desc', 'display_item_list', 'display_item_manual_sort', 'action_name_list', 'action_name_list_on_tab', 'activity_theme_id', 'is_activity_have_resident_part', 'is_resident_panel', 'resident_panel_unlock_module_id', 'daily_hint', 'finish_conditions', 'is_skip_switch_story_line')), ((0, (), None), (0, (), None), (0, (), None), (1, (), None), (2, ((0, (), None),), None), (1, (), None), (0, (), None), (0, (), None), (3,TextID,None), (3,TextID,None), (3,TextID,None), (1, (), None), (3,TextID,None), (3,TextID,None), (2, ((4,ItemConfig,None),), None), (0, (), (bool,())), (2, ((1, (), None),), None), (2, ((1, (), None),), None), (0, (), None), (0, (), (bool,())), (0, (), (bool,())), (0, (), None), (0, (), (bool,())), (2, ((4,ConditionParam,None),), None), (0, (), (bool,()))))
TalkSentenceConfig = (namedtuple('TalkSentenceConfig', ('talk_sentence_id', 'voice_id', 'textmap_talk_sentence_name', 'talk_sentence_text')), ((0, (), None), (0, (), None), (3,TextID,None), (3,TextID,None)))
MazeBuff = (namedtuple('MazeBuff', ('id', 'buff_series', 'buff_rarity', 'lv', 'lv_max', 'modifier_name', 'in_battle_binding_type', 'in_battle_binding_key', 'param_list', 'buff_desc_param_by_avatar_skill_id', 'buff_icon', 'buff_name', 'buff_desc', 'buff_simple_desc', 'buff_desc_battle', 'buff_effect', 'maze_buff_type', 'use_type', 'maze_buff_icon_type', 'maze_buff_pool', 'is_display', 'is_display_env_in_level')), ((0, (), None), (0, (), None), (0, (), None), (0, (), None), (0, (), None), (1, (), None), (0, (True,), (MazeBuffInBattleBindingType,())), (1, (), None), (2, ((0, (), (c,())),), None), (0, (), None), (1, (), None), (3,TextID,None), (3,TextID,None), (3,TextID,None), (3,TextID,None), (1, (), None), (0, (True,), (MazeBuffType,())), (0, (True,), (MazeBuffUseType,())), (0, (True,), (EnumStatusType,())), (0, (), None), (0, (), (bool,())), (0, (), (bool,()))))


def update_text_map(text_map):
	global _text_map
	_text_map = text_map


async def load_trans(design, language='CN'):
	data = await design.get_data(f'ExcelOutput/Textmap_{language.lower()}.bytes')
	update_text_map(SRTrans(data))
