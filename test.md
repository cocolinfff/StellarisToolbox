## <span title=civic_distinguished_admiralty style="border-bottom:1px dotted"> "海军传统"</span>
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   3
- - 拥有思潮:    "军国主义"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "干涉主义"
- -  "军国主义"

- text:    "是一定程度的§Y%ethic_fanatic_militarist%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - ship_fire_rate_mult:   0.1
- - command_limit_add:   10
- - ships_upkeep_mult:   -0.1
## <span title=civic_hive_subspace_ephapse style="border-bottom:1px dotted">civic_hive_subspace_ephapse</span>
- 随机权重:=>- 基础:   5
- 修正:=>- - country_naval_cap_mult:   0.20
- - councilor_gestalt_legion_exp_gain:   @gestalt_civic_node_xp_rate
- - ship_speed_mult:   0.20
- 前置条件:=>- 政体:=>- value:   auth_hive_mind
- swap_type:=>- trigger:=>- has_first_contact_dlc:   yes
## <span title=civic_hive_pooled_knowledge style="border-bottom:1px dotted">civic_hive_pooled_knowledge</span>
- 随机权重:=>- 基础:   5
- 前置条件:=>- 政体:=>- value:   auth_hive_mind
- 修正:=>- - species_leader_exp_gain:   0.25
- - councilor_gestalt_cognitive_exp_gain:   @gestalt_civic_node_xp_rate
- - country_leader_cap_add:   1
## <span title=civic_approaching_science style="border-bottom:1px dotted"> "走近科学"</span>
- 描述:    "—每成功研究一个科技，都将获得相当于两个月的凝聚力产出\n—人口额外生产 §Y0.5§! £physics£ £society£ £engineering£ 研究点数\n—人口额外消耗§Y0.25§!£consumer_goods£ %consumer_goods%"
- 需求:=>- 思潮:=>- value:    "机械主义"
- OR:=>- value:
- -  "宪政主义"
- -  "自由主义"

- text:    "是一定程度的§Y%ethic_fanatic_egalitarian%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   15
- 修正:=>- - 因子:   2
- - 拥有思潮:    "自由主义"
## <span title=civic_machine_anglers style="border-bottom:1px dotted">civic_machine_anglers</span>
- modification:   no
- playable:=>- has_aquatics:   yes
- ai_playable:=>- has_aquatics:   yes
- 描述:   civic_tooltip_machine_anglers_effects
- 需求:=>- species_archetype:=>- value:   MACHINE
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- icon:   gfx/interface/icons/governments/civics/civic_anglers.dds
- traits:=>- trait:   trait_robot_aquatic
- 随机权重:=>- 基础:   @civic_default_random_weight
## <span title=civic_machine_delegated_functions style="border-bottom:1px dotted">civic_machine_delegated_functions</span>
- 随机权重:=>- 基础:   5
- 前置条件:=>- 政体:=>- value:   auth_machine_intelligence
- 修正:=>- - councilor_gestalt_regulatory_exp_gain:   @gestalt_civic_node_xp_rate
- - leaders_upkeep_mult:   -0.3
- - country_leader_pool_size:   2
## <span title=civic_characteristic_socialism style="border-bottom:1px dotted"> "特色社会主义"</span>
- 描述:    "—开始游戏时解锁%reform_and_opening_up%政策。\n—针对新时代的新形势，我们要§E转换新思想§!，§Y提出新要求§!，§R拿出新方法§!，§B打开新局面§!，§M走向新征程§!。"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "竞争主义"
- -  "个人主义"

- text:    "是一定程度的§Y%ethic_fanatic_capitalism%§!"
- hide_modifiers:   yes
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   4
- - 拥有思潮:    "个人主义"
- 修正:=>- - job_core_party_members_per_pop:   0.02
- - job_merchant_per_pop:   0.02
- - planet_emigration_push_mult:   0.5
- - planet_jobs_slave_produces_mult:   0.1
- - country_pop_enslaved_mult:   0.15
- alternate_civic_version:    "%civic_characteristic_socialism%"
## <span title=civic_libido_equipment style="border-bottom:1px dotted"> "欲望器械"</span>
- modification:=>- add:=>- has_tradition:    "未来科技"
- 描述:    "—未采纳这个国民文化的国家对该文明的§Y评价§!§R-40§!，采纳了%civic_liberty_of_libido%国民文化的国家对该文明的§Y评价§!§R-100§!\n—能够建造 £building£ §Y%building_equipment_breeding_plant%§!\n—%job_tentacle_seedbed_effect_desc%\n—开始游戏时拥有§Y%tech_cloning%§!科技"
- swap_type:=>- trigger:=>- has_country_flag:   synthetic_empire
- 需求:=>- 思潮:=>- value:    "权威主义"
- NOR:=>- value:
- -  "和平主义"
- -  "道德主义"

- text:    "不接受任何程度的§Y道德主义§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   10
- 修正:=>- - pop_cat_worker_happiness:   -0.15
- - pop_cat_slave_happiness:   -0.3
- - pop_cat_ruler_happiness:   0.25
- - planet_pop_assembly_organic_mult:   0.15
- - pop_cat_ruler_political_power:   2
## <span title=civic_cultural_review_department style="border-bottom:1px dotted"> "文化审查部门"</span>
- 描述:    "—§R谁都不知道这个“灵活的标准程序”到底有什么存在的意义，我也一样。§!"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "单一主义"
- -  "排外主义"

- text:    "是一定程度的§Y%ethic_fanatic_xenophobe%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   0
## <span title=civic_the_song_of_gears style="border-bottom:1px dotted"> "齿轮之歌"</span>
- modification:=>- add:=>- has_tradition:    "未来科技"
- 描述:   civic_tooltip_the_song_of_gears_effects
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "技术主义"
- -  "机械主义"

- text:    "是一定程度的§Y%ethic_fanatic_materialist%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - planet_researchers_physics_research_produces_add:   -1
- - planet_researchers_engineering_research_produces_add:   1.5
- - category_materials_research_speed_mult:   0.66
- - category_computing_draw_chance_mult:   -0.99
- 随机权重:=>- 基础:   5
## <span title=civic_presence_fleet style="border-bottom:1px dotted"> "存在舰队"</span>
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   3
- - 拥有思潮:    "道德主义"
- 需求:=>- 思潮:=>- NOR:=>- value:
- -  "干涉主义"
- -  "军国主义"

- text:    "不接受任何程度的§Y军国主义§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - diplo_weight_naval_mult:   0.3
- - country_naval_coverage_mult:   3
- - ships_upkeep_mult:   -0.15
- - country_naval_cap_mult:   -0.3
## <span title=civic_machine_maintenance_protocols style="border-bottom:1px dotted">civic_machine_maintenance_protocols</span>
- 随机权重:=>- 基础:   5
- 描述:   civic_tooltip_machine_maintenance_protocols_effects
- 前置条件:=>- 政体:=>- value:   auth_machine_intelligence
- 修正:=>- - councilor_gestalt_growth_exp_gain:   @gestalt_civic_node_xp_rate
## <span title=civic_machine_toxic_baths style="border-bottom:1px dotted">civic_machine_toxic_baths</span>
- ai_playable:=>- has_toxoids:   yes
- 描述:   civic_tooltip_machine_toxic_baths_effects
- playable:=>- has_toxoids:   yes
- alternate_civic_version:   civic_toxic_baths_individual_machine
- 前置条件:=>- 政体:=>- value:   auth_machine_intelligence
- 需求:=>- origin:=>- NOT:=>- value:   origin_life_seeded
- 修正:=>- - councilor_gestalt_growth_exp_gain:   @gestalt_civic_node_xp_rate
## <span title=civic_guided_sapience style="border-bottom:1px dotted">"创世向导"</span>
- modification:=>- add:=>- has_tradition:    "未来科技"
- has_technology:   tech_epigenetic_triggers
- playable:=>- has_machine_age_dlc:   yes
- ai_playable:=>- has_machine_age_dlc:   yes
- 描述:   civic_tooltip_guided_sapience_effects
- 需求:=>- 思潮:=>- NOR:=>- value:
- -  "单一主义"
- -  "排外主义"

- text:    "不接受任何程度的§Y排外主义§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   @civic_rare_random_weight
- 修正:=>- - terraforming_cost_mult:   -0.25
- - terraform_speed_mult:   0.25
- negative_description:   civic_tooltip_guided_sapience_negative_effects
## <span title=civic_coalition_government_overlord style="border-bottom:1px dotted"> "联合政府"</span>
- 随机权重:=>- 基础:   5
- 描述:    "—你的§Y附属国§!不能签订含有以下条款的协议：\n——%t%%TRIGGER_FAIL%§Y%subject_cannot_expand%§!\n——%t%%TRIGGER_FAIL%§Y允许宗主国不加入附属国战争§!\n——%t%%TRIGGER_FAIL%§Y%subject_can_not_do_diplomacy%§!"
- 需求:=>- civics:=>- NOR:=>- value:
- -  "§H§Y主权邦联§!§!"
- -  "§H§Y封建王权§!§!"
- -  "§H§Y战争领主§!§!"

- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - country_naval_capacity_contribution_from_subjects_mult:   0.15
- - country_enclave_capacity_add:   1
- - empire_size_penalty_mult:   0.2
- - divided_patrongage_max_subjects:   2
- - pop_factions_produces_mult:   -0.15
## <span title=civic_forum_friends style="border-bottom:1px dotted"> "论坛水友"</span>
- modification:=>- add:=>- has_civic:    "%civic_forum_friends%"
- 描述:    "—游戏开始时将有§Y1~5个§!随机文明获得这一国民理念，而这些文明将会互相取得通讯并组建一个['concept_common_ground_federation']。\n—开始游戏时解锁§Y%tech_xeno_linguistics%§!科技"
- 需求:=>- 思潮:=>- NOR:=>- value:
- -  "单一主义"
- -  "排外主义"

- text:    "不接受任何程度的§Y排外主义§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- alternate_civic_version:    "%civic_forum_friends%"
- 随机权重:=>- 基础:   0
## <span title=civic_extremely_efficient_storage_corporate style="border-bottom:1px dotted"> "%civic_extremely_efficient_storage%"</span>
- 描述:    "—§Y%building_resource_silo%§!行星建筑额外§G+5000§!%MOD_COUNTRY_RESOURCE_MAX_ADD%，提高星球%MOD_POP_CITIZEN_HAPPINESS%并§G+1§!£job_soldier£ %job_soldier_plural%岗位\n—§Y%building_resource_silo%§!恒星基地建筑额外§G+5000§!%MOD_COUNTRY_RESOURCE_MAX_ADD%，并§G+1§!£unity£ %unity%\n—£building£§Y首都建筑§!提供的%MOD_COUNTRY_RESOURCE_MAX_ADD%翻倍"
- 修正:=>- - country_resource_max_minor_artifacts_add:   2500
- - country_resource_max_astral_threads_add:   250
- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- 随机权重:=>- 基础:   5
## <span title=civic_sovereign_guardianship style="border-bottom:1px dotted">civic_sovereign_guardianship</span>
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   5
- - 拥有思潮:    "排外主义"
- 描述:   civic_sovereign_guardianship_effects
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "单一主义"
- -  "排外主义"

- text:    "是一定程度的§Y%ethic_fanatic_xenophobe%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - starbase_defense_platform_capacity_add:   3
- - planet_orbital_bombardment_damage:   -0.25
- - country_border_friction_mult:   -0.15
- - army_defense_health_mult:   0.15
- - empire_size_systems_mult:   1
## <span title=civic_slaver_guilds style="border-bottom:1px dotted">civic_slaver_guilds</span>
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   5
- - 拥有思潮:    "权威主义"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "个人主义"
- -  "精英主义"
- -  "权威主义"

- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - planet_jobs_slave_produces_mult:   0.15
- - slave_market_cost_mult:   -0.15
## <span title=civic_master_engineer style="border-bottom:1px dotted"> "建筑公司"</span>
- 随机权重:=>- 基础:   10
- 修正:=>- - 因子:   2.5
- - 拥有思潮:    "军国主义"
- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- 修正:=>- - planet_building_build_speed_mult:   0.15
- - starbase_module_build_speed_mult:   0.15
- - starbase_building_build_speed_mult:   0.15
- - planet_max_buildings_add:   1
## <span title=civic_merchant_guilds style="border-bottom:1px dotted"> "§H§Y大康采恩§!§!"</span>
- 描述:    "—£building£ §Y首都建筑§!会替换部分 £job_politician£ §Y%job_politician%§!岗位为 £job_mogul£ §Y%job_mogul%§!岗位\n—£job_mogul£ %job_mogul_plural%额外§G+3%§!%mod_planet_jobs_energy_produces_mult%\n—能够通过战争夺取其他国家的§Y企业%BRANCH_OFFICES%§!\n—§Y市场经济§!下，无经济危机时，提供§Y-0.1§!%economic_situation_improve%"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "竞争主义"
- -  "个人主义"

- text:    "是一定程度的§Y%ethic_fanatic_capitalism%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - pop_cat_worker_happiness:   -0.1
- - branch_office_value_mult:   0.1
- - station_gatherers_produces_mult:   0.1
- - pop_ethic_capitalism_attraction_mult:   0.25
- 随机权重:=>- 基础:   60
- 修正:=>- - 因子:   0
- - has_civic:   civic_empty_vagrant
- - NOR:=>- has_origin:   origin_ev_both_choosen
- has_civic:   civic_ev_planet_and_fleet
- has_ascension_perk:   ev_land_planets
## <span title=civic_spiritual_seekers style="border-bottom:1px dotted"> "精神探寻者"</span>
- 描述:    "—寺庙建筑额外提供 £job_transcend£ %job_transcend%岗位，产生少量 £unity£ 凝聚力，£society£ 社会学研究和£engineering£ 工程学研究，并减少§Y£crime£ %PLANET_CRIME_TITLE%§!\n—出现§Y灵能理论§!科技选项的概率提高"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "和平主义"
- -  "道德主义"

- text:    "是一定程度的§Y%ethic_fanatic_pacifist%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   10
- 修正:=>- - 因子:   5
- - 拥有思潮:    "教权主义"
- 修正:=>- - LITHOID_POP_HAPPINESS:   0.1
- - biological_pop_happiness:   0.1
- - max_rivalries:   -2
- leader_background_job_weight:=>- transcend:   100
## <span title=civic_trading_posts style="border-bottom:1px dotted"> "贸易站点"</span>
- 描述:   civic_tooltip_trading_posts_effects
- 修正:=>- - starbase_trade_protection_mult:   0.25
- - country_starbase_capacity_add:   5
- - starbase_trade_collection_add:   2
- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   5
- - 拥有思潮:    "崇外主义"
## <span title=civic_parliamentary_system style="border-bottom:1px dotted"> "新民主"</span>
- 随机权重:=>- 基础:   1
- 修正:=>- - 因子:   15
- - 拥有思潮:    "个人主义"
- 需求:=>- 政体:=>- OR:=>- value:
- -  "寡头政治"
- -  "选举专制"

- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - country_unity_produces_mult:   0.25
- - pop_factions_produces_mult:   0.33
- - pop_growth_from_immigration:   0.25
- - country_base_influence_produces_add:   0.5
## <span title=civic_citizen_service style="border-bottom:1px dotted"> "§H§Y秩序军政§!§!"</span>
- 随机权重:=>- 基础:   60
- 修正:=>- - 因子:   0
- - has_civic:   civic_empty_vagrant
- - NOR:=>- has_origin:   origin_ev_both_choosen
- has_civic:   civic_ev_planet_and_fleet
- has_ascension_perk:   ev_land_planets
- 描述:    "—£building£ §Y首都建筑§!会替换部分 £job_politician£ §Y%job_politician%§!岗位为 £job_commandante£ §Y%job_commandante_plural%§!\n—£job_soldier£ §Y%job_soldier_plural%§!额外提高§Y2.5§! £stability£ %PLANET_STABILITY_TITLE%\n—取得一场战争的胜利后，获得相当于§Y三年§!产出的£unity£ §Y凝聚力§!，但如果战争失败，则§R%pop_citizen_happiness%§!将低迷§Y五年§!\n—开始游戏时解锁§Y%tech_combat_training%§!科技"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "干涉主义"
- -  "军国主义"

- text:    "是一定程度的§Y%ethic_fanatic_militarist%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - country_commander_cap_add:   2
- - armies_upkeep_mult:   0.1
- - country_war_exhaustion_mult:   -0.15
- - pop_ethic_militarist_attraction_mult:   0.25
## <span title=civic_du_contrat_social style="border-bottom:1px dotted"> "§E§H第三条路§!§!"</span>
- 描述:    "—奴隶可以担任所有的岗位\n—§Y奴隶§!人口额外产出§Y1§!£trade_value£ %TRADE_VALUE%"
- 需求:=>- 思潮:=>- NOR:=>- value:
- -  "自由主义"
- -  "集体主义"
- -  "权威主义"
- -  "个人主义"

- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - pop_cat_slave_happiness:   0.2
- - country_pop_enslaved_mult:   1
- - pop_category_slave_consumer_goods_upkeep_add:   0.4
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   0
- - has_civic:   civic_empty_vagrant
- - NOR:=>- has_origin:   origin_ev_both_choosen
- has_civic:   civic_ev_planet_and_fleet
- has_ascension_perk:   ev_land_planets
## <span title=civic_mining_company style="border-bottom:1px dotted"> "矿业公司"</span>
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   25
- - is_species_class:   LITHOID
- 需求:=>- civics:=>- NOR:=>- value:
- -  "自然卫士"
- -  "环保企业"

- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- 修正:=>- - planet_miners_minerals_produces_add:   2
- - planet_miners_energy_upkeep_add:   1
## <span title=civic_meritocracy style="border-bottom:1px dotted">1 "任人唯贤"</span>
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   5
- - 拥有思潮:    "自由主义"
- 描述:    "—领袖初始等级: §G+1§!"
- 需求:=>- 思潮:=>- NOR:=>- value:    "权威主义"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - planet_jobs_specialist_produces_mult:   0.1
- - pop_cat_specialist_political_power:   2
- - country_leader_pool_size:   2
## <span title=civic_warpdrive_start style="border-bottom:1px dotted"> "超越光芒"</span>
- modification:=>- add:=>- has_tradition:    "未来科技"
- 描述:   civic_tooltip_warpdrive_start_effects
- 需求:=>- civics:=>- NOR:=>- value:
- - civic_eager_explorers
- -  "私人航空集团"
- - civic_hive_stargazers
- - civic_machine_exploration_protocol
- -  "§E§H原始密教§!§!"

- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - country_starbase_influence_cost_mult:   -0.25
- - country_starbase_influence_cost_distance_mult:   -0.33
- 随机权重:=>- 基础:   5
## <span title=civic_terraforming style="border-bottom:1px dotted"> "园艺工程学"</span>
- modification:=>- add:=>- has_tradition:    "未来科技"
- 描述:    "—可以建造£building£ §Y%building_ranger_lodge%§!建筑，能够根据£blocker£ §Y星球自然障碍§!的数量提供£job_geoengineer£ §Y%job_geoengineer%§!岗位和£job_xenobiologist£ §Y%job_xenobiologist%§!岗位，并增加%MOD_PLANET_MAX_BUILDINGS_ADD%\n—允许使用特殊的星球决议，以根除星球的异常，例如§Y辐照天地§!、§Y潮汐锁定§!、§Y生态受损§!等等\n—能够通过星球决议添加£blocker£ §Y星球自然障碍§!\n—开始游戏时解锁§Y地表塑造§!科技"
- 需求:=>- 思潮:=>- value:    "机械主义"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   5
- 修正:=>- - planet_decision_enact_speed_mult:   0.25
- - terraforming_cost_mult:   -0.33
- - category_new_worlds_research_speed_mult:   0.25
## <span title=civic_financial_investment style="border-bottom:1px dotted"> "金融投资"</span>
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   5
- - 拥有思潮:    "个人主义"
- 描述:   civic_tooltip_financial_investment_effects
- 需求:=>- 思潮:=>- NOR:=>- value:    "集体主义"
- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- 修正:=>- - planet_technician_energy_produces_add:   -0.5
## <span title=civic_individual_machine_warbots_corporate style="border-bottom:1px dotted"> "%civic_individual_machine_warbots%"</span>
- ai_weight:=>- 基础:   @ai_civic_default_base_weight
- 修正:=>- - 因子:   @ai_civic_personality_mismatch_factor
- 随机权重:=>- 基础:   @civic_default_random_weight
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "干涉主义"
- -  "军国主义"

- text:    "是一定程度的§Y%ethic_fanatic_militarist%§!"
- 前置条件:=>- species_archetype:=>- value:   MACHINE
- 修正:=>- - army_damage_mult:   0.25
- - commander_exp_gain:   0.15
- - armies_upkeep_mult:   -0.25
## <span title=civic_machine_astromining_drones style="border-bottom:1px dotted">civic_machine_astromining_drones</span>
- ai_playable:=>- has_megacorp:   yes
- 描述:   civic_tooltip_machine_astromining_drones_effects
- playable:=>- has_megacorp:   yes
- 前置条件:=>- 政体:=>- value:   auth_machine_intelligence
- 随机权重:=>- 基础:   @civic_rare_random_weight
- 修正:=>- - stations_cost_mult:   -0.50
- - planet_jobs_simple_drone_produces_mult:   -0.50
- - country_starbase_capacity_mult:   0.50
- - station_gatherers_produces_mult:   0.5
- - councilor_gestalt_growth_exp_gain:   @gestalt_civic_node_xp_rate
- ai_weight:=>- 基础:   @ai_civic_uncommon_base_weight
## <span title=civic_peacekeepers style="border-bottom:1px dotted"> "普世主义"</span>
- 随机权重:=>- 基础:   25
- 描述:    "—在§Y联邦§!中时，维持§Y互不侵犯协定§!和§Y研究协议§!不花费影响力 \n—在§Y联邦§!中时§Y异族主义§!派系提供额外的认同 \n—成功的§Y提升土著§!给予10年帝国范围修正，提高 £unity£ 凝聚力和 £society£ 社会学研究\n—不能拥有§Y宿敌§!"
- 需求:=>- 思潮:=>- value:    "崇外主义"
- OR:=>- value:
- -  "和平主义"
- -  "道德主义"

- text:    "是一定程度的§Y%ethic_fanatic_pacifist%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - diplomacy_upkeep_mult:   -0.15
- - envoys_add:   3
- - diplo_weight_mult:   0.25
- - country_border_friction_mult:   -0.5
- - envoy_improve_relations_mult:   0.15
- - ship_weapon_damage:   -0.15
## <span title=civic_martial_brotherhood style="border-bottom:1px dotted"> "人民军队"</span>
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   5
- - 拥有思潮:    "集体主义"
- 描述:    "—§Y军事领袖§!维护费用减半\n—戒严时不会减少§Y%mod_planet_jobs_produces_mult%§!\n—£defense_army£§Y防御部队§!现在会提供少量%r_energy%、%r_minerals%、%r_food%与%r_unity%\n—动员出的部队将无需§Y维护费§!，且升级为更强大的§Y民兵§!"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "宪政主义"
- -  "自由主义"
- -  "干涉主义"
- -  "军国主义"

- text:    "一定程度上偏向§Y%ethic_fanatic_egalitarian%§!或者§Y%ethic_fanatic_militarist%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - army_defense_morale_mult:   0.5
- - army_collateral_damage_mult:   -0.5
## <span title=civic_ultimate_collective style="border-bottom:1px dotted">1 "§H§Y全息之眼§!§!"</span>
- 描述:    "—£building£ §Y首都建筑§!会替换部分 £job_politician£ §Y%job_politician%§!岗位为 £job_core_party_members£ §Y%job_core_party_members_plural%§!\n—§Y%pop_cat_ruler%§!阶级额外产出§Y0.25§!£physics_research£ £engineering_research£ £society_research£ 研究点数\n—£job_enforcer£ §Y%job_enforcer_plural%§!额外产出§Y5§! £unity£ 凝聚力\n—允许特殊法令——§Y%edict_immortal_ruler%§!，能使当前的统治者不朽"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "竞争主义"
- -  "个人主义"

- text:    "是一定程度的§Y%ethic_fanatic_capitalism%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - intel_encryption_add:   1
- - country_base_influence_produces_add:   1
- - planet_structures_upkeep_mult:   0.1
- - pop_ethic_authoritarian_attraction_mult:   0.25
- 随机权重:=>- 基础:   60
- 修正:=>- - 因子:   0
- - has_civic:   civic_empty_vagrant
- - NOR:=>- has_origin:   origin_ev_both_choosen
- has_civic:   civic_ev_planet_and_fleet
- has_ascension_perk:   ev_land_planets
## <span title=civic_hive_one_mind style="border-bottom:1px dotted">civic_hive_one_mind</span>
- 随机权重:=>- 基础:   5
- 需求:=>- civics:=>- NOR:=>- value:
- -  "天然神经网络"
- - civic_hive_divided_attention

- 前置条件:=>- 政体:=>- value:   auth_hive_mind
- 修正:=>- - councilor_gestalt_regulatory_exp_gain:   @gestalt_civic_node_xp_rate
- - country_unity_produces_mult:   0.25
- - negative_traits_country:   -1
## <span title=civic_ideal_slavery style="border-bottom:1px dotted"> "理想奴隶制"</span>
- 描述:    "—不能延长法定工作时间\n—必须采用奴隶制\n—§Y奴隶§!人口额外消耗§Y0.5§!£building£ %MOD_PLANET_HOUSING_ADD%"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "和平主义"
- -  "道德主义"

- text:    "是一定程度的§Y%ethic_fanatic_pacifist%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - pop_cat_slave_political_power:   1
- - pop_cat_slave_happiness:   0.2
- - pop_category_slave_consumer_goods_upkeep_add:   0.2
- 随机权重:=>- 基础:   15
- 修正:=>- - 因子:   3
- - 拥有思潮:    "集体主义"
## <span title=civic_machine_replication style="border-bottom:1px dotted">civic_machine_replication</span>
- 随机权重:=>- 基础:   5
- 前置条件:=>- 政体:=>- value:   auth_machine_intelligence
- 修正:=>- - councilor_gestalt_growth_exp_gain:   @gestalt_civic_node_xp_rate
- - planet_pop_assembly_mult:   0.25
## <span title=civic_underworld_society style="border-bottom:1px dotted"> "黑社会"</span>
- 描述:    "—不能签署§Y商业协议§!\n—可以在任何未与自己处于战争中或停战中的帝国的星球上建立§Y分部§!\n—能够在自己的星球上设立§Y分部§!\n—§Y分部§!行星上的£crime£ %PLANET_CRIME_TITLE%会提高分部的价值\n—可以建设独特的增加£crime£ %PLANET_CRIME_TITLE%的 £building£ §Y%BRANCH_OFFICE_BUILDINGS%§!，这些建筑会提高自己星球的£stability£%PLANET_STABILITY_TITLE%\n—每个§Y%job_criminal%§!提高§G2%§!当地劳工人口产出，并且额外增加§Y1§!£stability£%PLANET_STABILITY_TITLE%"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "干涉主义"
- -  "军国主义"

- text:    "是一定程度的§Y%ethic_fanatic_militarist%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   1
- 修正:=>- - 因子:   15
- - 拥有思潮:    "个人主义"
## <span title=civic_juvenile_culture style="border-bottom:1px dotted"> "幼崽文化"</span>
- 描述:   civic_tooltip_juvenile_culture_effects
- 需求:=>- civics:=>- NOR:=>- value:
- -  "血源诅咒"
- -  "父父子子"
- -  "逐火之蛾"
- - civic_ruthless_competition

- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - s_slot_weapon_fire_rate_mult:   0.15
- - shipsize_corvette_build_speed_mult:   0.15
- - category_particles_research_speed_mult:   0.15
- - shipsize_frigate_build_speed_mult:   0.15
## <span title=civic_echoes_of_suffering style="border-bottom:1px dotted"> "苦难回响"</span>
- ai_playable:=>- host_has_dlc:   HumanoidsSpeciesPack
- 描述:   civic_tooltip_echoes_of_suffering_effects
- playable:=>- host_has_dlc:   HumanoidsSpeciesPack
- 需求:=>- species_archetype:=>- NOR:=>- value:
- - LITHOID
- - MACHINE

- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   5
## <span title=civic_hive_stargazers style="border-bottom:1px dotted">civic_hive_stargazers</span>
- modification:   no
- playable:=>- has_first_contact_dlc:   yes
- ai_playable:=>- has_first_contact_dlc:   yes
- 描述:   civic_hive_stargazers_effects
- 需求:=>- origin:=>- NOR:=>- value:
- -  "厚积薄发"
- -  "异星歧途"

- 前置条件:=>- 政体:=>- value:   auth_hive_mind
- 修正:=>- - ship_sensor_range_add:   1
- - councilor_gestalt_legion_exp_gain:   @gestalt_civic_node_xp_rate
- - ship_hyperlane_range_add:   2
- - country_starbase_influence_cost_distance_mult:   -0.2
- traits:=>- trait:   trait_stargazer
- 随机权重:=>- 基础:   0
## <span title=civic_human_rights_first style="border-bottom:1px dotted"> "人杈至上"</span>
- 描述:    "—能够使用§B“为了人杈”§!战争理由\n—§R不能与战争中的国家签订§Y商业条约§!§!"
- 需求:=>- 政体:=>- NOT:=>- value:    "世袭专制"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - pop_growth_from_immigration:   0.15
- - country_power_projection_influence_produces_add:   1
- - country_claim_influence_cost_mult:   -0.15
- - planet_stability_add:   -5
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   0
- - 拥有思潮:    "自由主义"
## <span title=civic_real_estate_market_corporate style="border-bottom:1px dotted"> "房产企业"</span>
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   4
- - 拥有思潮:    "个人主义"
- 描述:    "—§Y住房区划§!额外提供£trade_value£ %TRADE_VALUE%，但§R减少§!£housing£ %PLANET_HOUSING_TITLE%\n—§Y住房建筑§!额外提供£job_manager£ %job_manager_plural%岗位，但增加§R1§!£crime£ %PLANET_CRIME_TITLE%"
- 需求:=>- 思潮:=>- NOR:=>- value:    "集体主义"
- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- 修正:=>- - pop_cat_worker_happiness:   -0.05
- - job_merchant_add:   1
## <span title=civic_free_traders style="border-bottom:1px dotted">civic_free_traders</span>
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "宪政主义"
- -  "自由主义"

- text:    "是一定程度的§Y%ethic_fanatic_egalitarian%§!"
- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- 修正:=>- - country_trade_attractiveness:   0.15
- - trade_value_mult:   0.2
- - branch_office_value_mult:   0.25
- 随机权重:=>- 基础:   25
- 修正:=>- - 因子:   5
- - 拥有思潮:    "崇外主义"
## <span title=civic_brand_loyalty style="border-bottom:1px dotted">civic_brand_loyalty</span>
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "精神主义"
- -  "教权主义"

- text:    "是一定程度的§Y%ethic_fanatic_spiritualist%§!"
- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- 修正:=>- - country_unity_produces_mult:   0.15
- - pop_government_ethic_attraction:   0.5
- 随机权重:=>- 基础:   25
## <span title=civic_peaceful_republic style="border-bottom:1px dotted"> "§H§Y和平乌托邦§!§!"</span>
- 随机权重:=>- 基础:   60
- 修正:=>- - 因子:   0
- - has_civic:   civic_empty_vagrant
- - NOR:=>- has_origin:   origin_ev_both_choosen
- has_civic:   civic_ev_planet_and_fleet
- has_ascension_perk:   ev_land_planets
- 描述:    "—£building£ §Y首都建筑§!会替换部分 £job_politician£ §Y%job_politician%§!岗位为 £job_supervisor£ §Y%job_supervisor_plural%§!。\n—£job_bureaucrat£ §Y%job_bureaucrat_plural%§!额外提高§Y2§! £stability£ %PLANET_STABILITY_TITLE%。\n—和平每持续十年，%pop_citizen_happiness%就§G+10%§!，这一效果上限为§Y50%§!。\n—§Y领袖§!有§Y20%§!几率初始自带额外的正面及负面特质各一个。"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "和平主义"
- -  "道德主义"

- text:    "是一定程度的§Y%ethic_fanatic_pacifist%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - country_admin_cap_mult:   0.33
- - country_war_exhaustion_mult:   0.25
- - planet_bureaucrats_upkeep_mult:   -0.25
- - pop_ethic_pacifist_attraction_mult:   0.25
## <span title=civic_scavengers style="border-bottom:1px dotted">civic_scavengers</span>
- ai_playable:=>- OR:=>- has_toxoids:   yes
- has_overlord_dlc:   yes
- 描述:   civic_scavengers_effects
- playable:=>- OR:=>- has_toxoids:   yes
- has_overlord_dlc:   yes
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   15
- - has_origin:   origin_post_apocalyptic
## <span title=civic_corvee_system style="border-bottom:1px dotted">civic_corvee_system</span>
- 随机权重:=>- 基础:   10
- 修正:=>- - 因子:   2.5
- - is_authoritarian:   yes
- 描述:   civic_corvee_system_effects
- 需求:=>- 思潮:=>- NOR:=>- value:
- -  "宪政主义"
- -  "自由主义"

- text:    "不接受任何程度的§Y自由主义§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - pop_growth_from_immigration:   0.15
- - planet_jobs_worker_produces_mult:   0.05
## <span title=civic_labor_aristocracy style="border-bottom:1px dotted"> "§H§Y工人贵族§!§!"</span>
- 描述:    "—£building£ §Y首都建筑§!会替换部分 £job_politician£ §Y%job_politician%§!岗位为 £job_noble£ §Y%job_noble_plural%§!岗位。\n—%job_noble_effect_soc_desc%。\n—£pop_cat_ruler£ §Y%pop_cat_ruler%§!阶级额外产出§Y0.25§!£physics_research£ £engineering_research£ £society_research£ 研究点数。\n—根据领袖类型，£ruler£ §Y统治者§!领袖额外产出£consumer_goods£ 消费品或£alloys£ 合金。"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "合作主义"
- -  "集体主义"

- text:    "是一定程度的§Y%ethic_fanatic_socialism%§!"
- leader_background_job_weight:=>- "foundry_specialist":   25
- "artisan_specialist":   25
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   60
- 修正:=>- - 因子:   0
- - has_civic:   civic_empty_vagrant
- - NOR:=>- has_origin:   origin_ev_both_choosen
- has_civic:   civic_ev_planet_and_fleet
- has_ascension_perk:   ev_land_planets
- 修正:=>- - councilor_exp_gain:   0.33
- - planet_jobs_ruler_produces_mult:   0.15
- - pop_category_rulers_upkeep_mult:   0.1
- - pop_ethic_socialism_attraction_mult:   0.25
## <span title=civic_machine_exploration_protocol style="border-bottom:1px dotted">civic_machine_exploration_protocol</span>
- modification:=>- add:=>- has_technology:   tech_subspace_drive
- playable:=>- has_first_contact_dlc:   yes
- alternate_civic_version:   civic_eager_explorers
- ai_playable:=>- has_first_contact_dlc:   yes
- 描述:   civic_machine_exploration_protocol_effects
- 需求:=>- origin:=>- NOR:=>- value:
- -  "厚积薄发"
- -  "异星歧途"

- 前置条件:=>- 政体:=>- value:   auth_machine_intelligence
- 修正:=>- - first_contact_speed_mult:   0.2
- - councilor_gestalt_legion_exp_gain:   @gestalt_civic_node_xp_rate
- - station_observers_unity_produces_add:   3
- 随机权重:=>- 基础:   0
## <span title=civic_futuristic_art style="border-bottom:1px dotted"> "未来派艺术"</span>
- 描述:    "—£job_researcher£ %job_researcher_plural%与£job_head_researcher£ %job_head_researcher_plural%额外产出§Y0.5§!£unity£ 凝聚力\n—£job_entertainer£ %job_entertainer_plural%额外产出£physics£ £society£ £engineering£ ，但提供的£mod_planet_amenities_add£ %PLANET_AMENITIES_TITLE%§R-2§!\n—§Y%building_autochthon_monument%§!与§Y%building_galactic_memorial_1%§!额外产生£physics£ £society£ £engineering£ "
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "技术主义"
- -  "机械主义"

- text:    "是一定程度的§Y%ethic_fanatic_materialist%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   10
- 修正:=>- - 因子:   5
- - has_civic:    "艺术国度"
- 修正:=>- - planet_entertainers_engineering_research_produces_add:   2
- - country_unity_produces_mult:   0.10
- - planet_entertainers_physics_research_produces_add:   2
- - planet_entertainers_society_research_produces_add:   2
- swap_type:=>- 描述:    "—£job_researcher£ %job_researcher_plural%与£job_head_researcher£ %job_head_researcher_plural%额外产出§Y0.5§!£unity£ 凝聚力\n—£job_duelist£ %job_duelist_plural%额外产出£physics£ £engineering£ ，但提供的£mod_planet_amenities_add£ %PLANET_AMENITIES_TITLE%§R-2§!\n—§Y%building_autochthon_monument%§!与§Y%building_galactic_memorial_1%§!额外产生£physics£ £society£ £engineering£ "
- trigger:=>- is_duelist_country:   yes
## <span title=civic_real_estate_market style="border-bottom:1px dotted"> "房产市场"</span>
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   4
- - 拥有思潮:    "个人主义"
- 描述:    "—§Y住房区划§!额外提供£trade_value£ %TRADE_VALUE%，但§R减少§!£housing£ %PLANET_HOUSING_TITLE%\n—§Y住房建筑§!额外提供£job_manager£ %job_manager_plural%岗位，但增加§R1§!£crime£ %PLANET_CRIME_TITLE%"
- 需求:=>- 思潮:=>- NOR:=>- value:    "集体主义"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - pop_cat_worker_happiness:   -0.05
- - job_merchant_add:   1
## <span title=civic_constitutional_monarchy style="border-bottom:1px dotted"> "大宪章"</span>
- 需求:=>- 政体:=>- OR:=>- value:
- -  "间接民主"
- -  "寡头政治"
- -  "选举专制"

- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   1
- 修正:=>- - 因子:   15
- - 拥有思潮:    "个人主义"
## <span title=civic_machine_obsessional_directive style="border-bottom:1px dotted">civic_machine_obsessional_directive</span>
- modification:=>- add:=>- has_tradition:    "未来传统完成"
- has_technology:   tech_ascension_theory
- ai_playable:=>- has_machine_age_dlc:   yes
- playable:=>- has_machine_age_dlc:   yes
- 描述:   civic_machine_obsessional_directive_effects
- 需求:=>- civics:=>- NOT:=>- value:   civic_machine_warbots
- 前置条件:=>- 政体:=>- value:   auth_machine_intelligence
- 修正:=>- - planet_jobs_produces_mult:   0.2
- - councilor_gestalt_growth_exp_gain:   @gestalt_civic_node_xp_rate
- 随机权重:=>- 修正:=>- - 因子:   10
- - has_civic:    "金融投资网络"
## <span title=civic_cutthroat_politics style="border-bottom:1px dotted"> "阴谋政治"</span>
- 需求:=>- 思潮:=>- NOR:=>- value:
- -  "崇外主义"
- -  "道德主义"

- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - intel_encryption_add:   1
- - ship_cloaking_strength_add:   2
- - country_election_cost_mult:   -0.75
- - spy_network_value_add:   1
- - country_trust_cap_add:   -25
- 随机权重:=>- 基础:   10
- 修正:=>- - 因子:   2.5
- - is_authoritarian:   yes
## <span title=civic_presence_fleet_corporate style="border-bottom:1px dotted"> "存在舰队"</span>
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   3
- - 拥有思潮:    "道德主义"
- 需求:=>- 思潮:=>- NOR:=>- value:
- -  "干涉主义"
- -  "军国主义"

- text:    "不接受任何程度的§Y军国主义§!"
- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- 修正:=>- - diplo_weight_naval_mult:   0.3
- - country_naval_coverage_mult:   3
- - ships_upkeep_mult:   -0.15
- - country_naval_cap_mult:   -0.3
## <span title=civic_memory_vault_machine style="border-bottom:1px dotted">civic_memory_vault_machine</span>
- ai_playable:=>- host_has_dlc:   GalacticParagons
- 描述:   civic_tooltip_memory_vault_machine_effects
- playable:=>- host_has_dlc:   GalacticParagons
- 需求:=>- civics:=>- NOT:=>- value:   civic_memory_vault
- 前置条件:=>- 政体:=>- value:   auth_machine_intelligence
- 随机权重:=>- 基础:   4
- 修正:=>- - councilor_gestalt_cognitive_exp_gain:   @gestalt_civic_node_xp_rate
- - councilor_skill_add:   1
## <span title=civic_spiritual_democracy style="border-bottom:1px dotted"> "§H§Y圣灵议会§!§!"</span>
- 随机权重:=>- 基础:   60
- 修正:=>- - 因子:   0
- - has_civic:   civic_empty_vagrant
- - NOR:=>- has_origin:   origin_ev_both_choosen
- has_civic:   civic_ev_planet_and_fleet
- has_ascension_perk:   ev_land_planets
- 描述:    "—£building£ §Y首都建筑§!会替换部分 £job_politician£ §Y%job_politician%§!岗位为 £job_high_priest£ §Y%job_high_priest_plural%§!。\n—£job_priest£ %job_priest_plural%会额外产出§Y1§! £stability£ %PLANET_STABILITY_TITLE%并减少§Y%MOD_SPECIES_EMPIRE_SIZE_MULT%§!。\n—§Y%LEADER_ISWAS_COUNCILOR_SHORT%§!每五年都可以获得一个§Y随机%TRAITS%§!。\n—禁止§Y奴役§!本种族人，不允许§Y人口控制§!。"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "精神主义"
- -  "教权主义"

- text:    "是一定程度的§Y%ethic_fanatic_spiritualist%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - empire_size_pops_mult:   -0.15
- - tradition_cost_empire_size_mult:   -0.5
- - pop_ethics_shift_speed_mult:   -1
- - pop_ethic_spiritualist_attraction_mult:   0.25
## <span title=civic_private_prospectors style="border-bottom:1px dotted"> "民营勘探者"</span>
- 描述:   civic_tooltip_private_prospectors_effects
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "宪政主义"
- -  "自由主义"

- text:    "是一定程度的§Y%ethic_fanatic_egalitarian%§!"
- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- 修正:=>- - colony_start_num_pops_add:   1
- - empire_size_systems_mult:   -0.33
- 随机权重:=>- 基础:   25
- 修正:=>- - 因子:   2
- - 拥有思潮:    "排外主义"
## <span title=civic_machine_builder style="border-bottom:1px dotted">civic_machine_builder</span>
- 随机权重:=>- 基础:   5
- 描述:   civic_tooltip_functional_architecture_effects
- 前置条件:=>- 政体:=>- value:   auth_machine_intelligence
- 修正:=>- - councilor_gestalt_growth_exp_gain:   @gestalt_civic_node_xp_rate
- - planet_structures_upkeep_mult:   -0.2
- - planet_structures_cost_mult:   -0.2
- - planet_max_buildings_add:   2
## <span title=civic_business_reporting_administration style="border-bottom:1px dotted"> "商业报告行政"</span>
- 描述:    "—替换 £job_manager£ §Y%job_manager_plural%§!岗位为 £job_clerk£ §Y%job_clerk%§!岗位， £job_clerk£ §Y%job_clerk%§!额外产出少量的§Y%MOD_COUNTRY_ADMIN_CAP_ADD%§!\n—开始游戏时解锁§Y%tech_effective_bureaucracy%§!科技"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "宪政主义"
- -  "自由主义"

- text:    "是一定程度的§Y%ethic_fanatic_egalitarian%§!"
- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- 随机权重:=>- 基础:   10
- 修正:=>- - 因子:   0
- - is_species_class:   HUM
## <span title=civic_political_pluralism style="border-bottom:1px dotted"> "政治多元化"</span>
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   5
- - 拥有思潮:    "自由主义"
- 描述:    "—不能驱逐派系"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "宪政主义"
- -  "自由主义"

- text:    "是一定程度的§Y%ethic_fanatic_egalitarian%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - country_leader_pool_size:   2
- - pop_cat_worker_political_power:   1
- - country_election_cost_mult:   2
- - pop_factions_unity_produces_add:   0.25
- - pop_citizen_happiness:   0.1
- - pop_cat_specialist_political_power:   1
- - pop_ethic_authoritarian_attraction_mult:   -0.15
## <span title=civic_consumerism style="border-bottom:1px dotted"> "奢侈消费主义"</span>
- 随机权重:=>- 基础:   10
- 修正:=>- - 因子:   5
- - 拥有思潮:    "个人主义"
- 描述:    "—£job_artisan£ %job_artisan_specialist_plural%与£job_artisan£ %job_artisan_plural%额外产出£trade_value£ %TRADE_VALUE%\n—§Y工业区划§!提供额外 £job_trader£ %job_trader_plural%岗位\n—§Y商业区§!、§Y商业复合体§!建筑和§Y城市区划§!提供额外£job_artisan£ %job_artisan_plural%岗位\n—§Y企业家派系§!会因§Y加强环境监管§!政策不悦，对§Y轻工业补贴§!税收投资政策感到愉悦\n—§Y市场经济§!下, 无经济危机时, 提供§Y+0.3§!%economic_situation_improve%。"
- 需求:=>- 思潮:=>- NOR:=>- value:
- -  "集体主义"
- -  "教权主义"

- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - pop_category_workers_consumer_goods_upkeep_add:   0.25
- - pop_category_specialists_consumer_goods_upkeep_add:   0.75
- - pop_lifestyle_trade_mult:   0.35
- - pop_category_rulers_consumer_goods_upkeep_add:   1.5
- - planet_artisans_minerals_upkeep_add:   1
- - pop_ethic_capitalism_attraction_mult:   0.15
## <span title=civic_dark_consortium style="border-bottom:1px dotted">"奥术神座"</span>
- modification:=>- add:=>- has_tradition:    "未来科技"
- has_technology:   tech_mine_dark_matter
- playable:=>- has_astral_planes_dlc:   yes
- ai_playable:=>- has_astral_planes_dlc:   yes
- 描述:   civic_dark_consortium_effects
- 需求:=>- civics:=>- NOT:=>- value:    "§E§H原始密教§!§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- ai_weight:=>- 基础:   @civic_rare_random_weight
- 随机权重:=>- 基础:   @civic_rare_random_weight
- 修正:=>- - category_field_manipulation_research_speed_mult:   0.15
- - country_sr_dark_matter_produces_mult:   0.15
- - category_materials_research_speed_mult:   0.15
## <span title=civic_superhuman_economy_corporate style="border-bottom:1px dotted"> "投资之神"</span>
- 描述:   civic_tooltip_superhuman_economy_effects
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "精英主义"
- -  "权威主义"

- text:    "是一定程度的§Y%ethic_fanatic_authoritarian%§!"
- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- 修正:=>- - leaders_cost_mult:   0.25
- - leaders_upkeep_mult:   0.25
- - councilor_skill_add:   3
- - planet_jobs_produces_mult:   -0.25
## <span title=civic_machine_diplomatic_protocols style="border-bottom:1px dotted">civic_machine_diplomatic_protocols</span>
- ai_playable:=>- has_machine_age_dlc:   yes
- playable:=>- has_machine_age_dlc:   yes
- 需求:=>- civics:=>- NOT:=>- value:   civic_machine_terminator
- 前置条件:=>- 政体:=>- value:   auth_machine_intelligence
- ai_weight:=>- 基础:   @civic_rare_random_weight
- 随机权重:=>- 基础:   @civic_rare_random_weight
- 修正:=>- - envoys_add:   2
- - councilor_gestalt_regulatory_exp_gain:   @gestalt_civic_node_xp_rate
- - diplo_weight_mult:   0.25
- - country_trust_cap_add:   35
- - envoy_improve_relations_mult:   0.50
## <span title=civic_privatized_exploration style="border-bottom:1px dotted"> "私人航空集团"</span>
- modification:=>- add:=>- has_technology:   tech_subspace_drive
- 描述:   civic_privatized_exploration_effects
- playable:=>- has_first_contact_dlc:   yes
- alternate_civic_version:   civic_eager_explorers
- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- 需求:=>- origin:=>- NOR:=>- value:
- -  "厚积薄发"
- -  "异星歧途"
- - origin_payback
- - origin_broken_shackles
- - origin_fear_of_the_dark

- 修正:=>- - starbase_module_build_speed_mult:   0.15
- - starbase_building_build_speed_mult:   0.15
- - starbase_upgrade_speed_mult:   0.15
- 随机权重:=>- 基础:   0
## <span title=civic_toxic_baths style="border-bottom:1px dotted"> "诱变水疗中心"</span>
- modification:=>- add:=>- has_tradition:    "未来科技"
- playable:=>- has_toxoids:   yes
- alternate_civic_version:   civic_toxic_baths_individual_machine
- ai_playable:=>- has_toxoids:   yes
- 描述:   civic_tooltip_toxic_baths_effects
- 需求:=>- origin:=>- NOT:=>- value:   origin_life_seeded
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   15
- 修正:=>- - 因子:   4
- - owner_main_species:=>- is_species_class:   TOX
- leader_background_job_weight:=>- bath_attendant:   50
## <span title=civic_altruism style="border-bottom:1px dotted"> "§E§H利他主义§!§!"</span>
- 描述:    "—对§H非灭绝者文明§!的好感§G+1000§!\n—每个大使馆§G+10§! £unity£ 凝聚力\n—§Y失业人口§!额外产出§Y2§!£unity£ 凝聚力\n—不能§Y要求其他国家成为朝贡国§!\n—不能§Y关闭边界§!"
- playable:=>- host_has_dlc:   Utopia
- 需求:=>- 思潮:=>- value:    "崇外主义"
- OR:=>- value:
- -  "道德主义"
- -  "教权主义"

- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   75
- 修正:=>- - 因子:   0
- - NOT:=>- host_has_dlc:   Utopia
- 修正:=>- - diplomacy_upkeep_mult:   -1
- - max_rivalries:   -250
- - country_trust_cap_add:   1000
- - country_trust_growth:   1
- - diplo_weight_mult:   2.5
- - country_power_projection_influence_produces_mult:   -1
- - planet_pops_unemployed_consumer_goods_upkeep_add:   1
- - pop_ethic_xenophile_attraction_mult:   0.25
## <span title=civic_diplomatic_corps style="border-bottom:1px dotted">civic_diplomatic_corps</span>
- playable:=>- host_has_dlc:   Federations
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "多元主义"
- -  "崇外主义"

- text:    "是一定程度的§Y%ethic_fanatic_xenophile%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - envoys_add:   2
- - diplo_weight_mult:   0.2
- - country_trust_growth:   0.3
- 随机权重:=>- 基础:   10
- 修正:=>- - 因子:   2.5
- - 拥有思潮:    "崇外主义"
## <span title=civic_industrial_automatation_corporate style="border-bottom:1px dotted"> "创新基金"</span>
- 描述:    "—£job_merchant£ %job_merchant_plural%、£job_manager£ %job_manager_plural%和£job_trader£ %job_trader_plural%额外生产£physics£ £society£ £engineering£\n—£job_researcher£%job_researcher_plural%岗位提供额外的£trade_value£ %TRADE_VALUE%\n—开始游戏时解锁%trade_policy_unity%政策\n—§Y市场经济§!下, 无经济危机时, 提供§Y+0.1§!%economic_situation_improve%和§Y+40§!%economic_crisis_threshold%。"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "技术主义"
- -  "机械主义"

- text:    "是一定程度的§Y%ethic_fanatic_materialist%§!"
- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- 修正:=>- - all_technology_research_speed:   0.1
- - country_unity_produces_mult:   -0.05
- 随机权重:=>- 基础:   25
## <span title=civic_galactic_uterus_corp style="border-bottom:1px dotted"> "基因银行"</span>
- 描述:   civic_galactic_uterus_effects
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "竞争主义"
- -  "个人主义"

- text:    "是一定程度的§Y%ethic_fanatic_capitalism%§!"
- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- 修正:=>- - pop_category_rulers_consumer_goods_upkeep_add:   0.5
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   5
- - 拥有思潮:    "个人主义"
## <span title=civic_enlightment style="border-bottom:1px dotted"> "和平国度"</span>
- 随机权重:=>- 基础:   10
- 修正:=>- - 拥有思潮:    "道德主义"
- - 因子:   3
- - NOT:=>- 拥有思潮:    "权威主义"
- 描述:    "—开始游戏时解锁§Y文化遗址§!科技，§Y教权主义§!开始游戏时解锁§Y全息仪式§!科技"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "和平主义"
- -  "道德主义"

- text:    "是一定程度的§Y%ethic_fanatic_pacifist%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - army_damage_mult:   -0.25
- - planet_jobs_produces_mult:   0.1
- - planet_amenities_mult:   0.15
- - trade_value_mult:   0.25
- - army_morale:   -0.25
## <span title=civic_memory_vault style="border-bottom:1px dotted">civic_memory_vault</span>
- ai_playable:=>- host_has_dlc:   GalacticParagons
- 描述:   civic_tooltip_memory_vault_effects
- playable:=>- host_has_dlc:   GalacticParagons
- 需求:=>- civics:=>- NOR:=>- value:
- -  "§E§H永远同在§!§!"
- - civic_memory_vault_hive
- - civic_memory_vault_machine

- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   3
- 修正:=>- - councilor_skill_add:   1
## <span title=civic_true_hero style="border-bottom:1px dotted"> "英雄本色"</span>
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "合作主义"
- -  "集体主义"

- text:    "是一定程度的§Y%ethic_fanatic_socialism%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - planet_labour_hero_produces_mult:   0.25
- - planet_amenities_mult:   0.1
- - biological_pop_happiness:   0.05
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   5
- - 拥有思潮:    "集体主义"
## <span title=civic_worker_coop style="border-bottom:1px dotted"> "§H§Y工团主义§!§!"</span>
- 描述:    "—£building£ §Y首都建筑§!会替换部分 £job_politician£ §Y%job_politician%§!岗位为 £job_labour_hero£ §Y%job_labour_hero%§!\n—§Y%pop_cat_worker%§!阶级额外产出§Y0.25§!£unity£ 凝聚力和§Y0.25§!£trade_value£ %TRADE_VALUE%，并额外消耗§Y0.15§!£consumer_goods£ 消费品\n—每个§Y采矿§!、§Y农业§!、§Y发电§!和§Y工业§!区划提供§G+2§!£housing£住房，但提高§R25%§!维护费。\n—§Y市场经济§!下, 无经济危机时, 提供§Y-10%§!%economic_crisis_accumulate%。"
- swap_type:=>- 描述:   civic_tooltip_firing_torch_communist_society_effects
- trigger:=>- is_egalitarian:   yes
- has_tradition:    "未来社会"
- is_xenophobe:   no
- is_democratic_country:   yes
- 拥有思潮:    "集体主义"
- has_technology:   tech_ascension_theory
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "宪政主义"
- -  "自由主义"

- text:    "是一定程度的§Y%ethic_fanatic_egalitarian%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - pop_job_trade_mult:   0.2
- - planet_worker_ownership_jobs_produces_mult:   0.2
- - planet_shared_burden_jobs_produces_mult:   -0.1
- - pop_ethic_socialism_attraction_mult:   0.25
- 随机权重:=>- 基础:   60
- 修正:=>- - 因子:   0
- - has_civic:   civic_empty_vagrant
- - NOR:=>- has_origin:   origin_ev_both_choosen
- has_civic:   civic_ev_planet_and_fleet
- has_ascension_perk:   ev_land_planets
## <span title=civic_private_healthcare_corporate style="border-bottom:1px dotted"> "医疗企业"</span>
- ai_playable:=>- host_has_dlc:   GalacticParagons
- 描述:   civic_tooltip_civic_private_healthcare_corporate_effects
- playable:=>- host_has_dlc:   GalacticParagons
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "和平主义"
- -  "道德主义"

- text:    "是一定程度的§Y%ethic_fanatic_pacifist%§!"
- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- 修正:=>- - job_healthcare_add:   3
- - leader_lifespan_add:   10
- - category_biology_research_speed_mult:   0.15
- 随机权重:=>- 基础:   25
- 修正:=>- - 因子:   1.5
- - 拥有思潮:    "排外主义"
## <span title=civic_nazbol style="border-bottom:1px dotted"> "§H§Y民族与阶级§!§!"</span>
- 描述:    "—£building£ §Y首都建筑§!会替换部分£job_politician£ §Y%job_politician%§!岗位为£job_core_party_members£ §Y%job_core_party_members_plural%§!，£job_labour_hero£ %job_labour_hero_plural%的产出类型将被替换\n—可以对其他国家使用§Y阶级斗争§!与§Y民族解放§!宣战借口\n—拥有§H%citizenship_full%§!的种族§Y%pop_cat_worker%§!阶级额外产出§Y0.5§!£unity£ 凝聚力，并额外消耗§Y0.25§!£consumer_goods£ 消费品\n—拥有§H%citizenship_full%§!的种族可采用§Y%living_standard_utopian%§!生活标准，无论其所属§Y阶层§!，在该标准下所有£pop£ 人口拥有丰富的£consumer_goods£ §Y%consumer_goods%§!维护费并享有同等§Y政治权力§!。"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "合作主义"
- -  "集体主义"

- text:    "是一定程度的§Y%ethic_fanatic_socialism%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   75
- 修正:=>- - 因子:   0
- - has_civic:   civic_empty_vagrant
- - NOR:=>- has_origin:   origin_ev_both_choosen
- has_civic:   civic_ev_planet_and_fleet
- has_ascension_perk:   ev_land_planets
- 修正:=>- - country_trust_growth:   -0.25
- - pop_ethic_xenophobe_attraction_mult:   0.2
- - country_war_exhaustion_mult:   -0.2
- - country_claim_influence_cost_mult:   -0.25
- - pop_ethic_socialism_attraction_mult:   0.2
- custom_tooltip_with_modifiers:   civic_sparta_spirit_effects_additional
## <span title=civic_permanent_employment style="border-bottom:1px dotted">"永身雇佣制"</span>
- modification:=>- add:=>- has_tradition:    "未来科技"
- ai_playable:=>- host_has_dlc:   NecroidsSpeciesPack
- playable:=>- host_has_dlc:   NecroidsSpeciesPack
- 描述:   civic_tooltip_permanent_employment_effects
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "竞争主义"
- -  "个人主义"

- text:    "是一定程度的§Y%ethic_fanatic_capitalism%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   15
- 修正:=>- - 因子:   5
- - has_origin:   origin_necrophage
- leader_background_job_weight:=>- reassigner:   100
## <span title=civic_industrial_automatation style="border-bottom:1px dotted"> "创新型经济"</span>
- 随机权重:=>- 基础:   10
- 修正:=>- - 因子:   2.5
- - 拥有思潮:    "机械主义"
- 描述:    "—£job_merchant£ %job_merchant_plural%、£job_manager£ %job_manager_plural%和£job_trader£ %job_trader_plural%额外生产£physics£ £society£ £engineering£\n—£job_researcher£%job_researcher_plural%岗位提供额外的£trade_value£ %TRADE_VALUE%\n—开始游戏时解锁%trade_policy_unity%政策\n—§Y市场经济§!下, 无经济危机时, 提供§Y+0.1§!%economic_situation_improve%和§Y+40§!%economic_crisis_threshold%。"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "技术主义"
- -  "机械主义"

- text:    "是一定程度的§Y%ethic_fanatic_materialist%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - all_technology_research_speed:   0.1
- - country_unity_produces_mult:   -0.05
## <span title=civic_hive_cordyceptic_drones style="border-bottom:1px dotted">civic_hive_cordyceptic_drones</span>
- ai_playable:=>- has_necroids:   yes
- 描述:   civic_tooltip_cordyceptic_drones
- playable:=>- has_necroids:   yes
- 需求:=>- OR:=>- origin:=>- value:   origin_necrophage
- 前置条件:=>- 政体:=>- value:   auth_hive_mind
- 修正:=>- - weapon_type_space_fauna_weapon_damage_mult:   0.5
- - councilor_gestalt_legion_exp_gain:   @gestalt_civic_node_xp_rate
- - weapon_type_space_fauna_weapon_fire_rate_mult:   0.5
## <span title=civic_private_militaries style="border-bottom:1px dotted"> "私人军队"</span>
- 描述:    "—§Y要塞§!和§Y堡垒§!建筑将£job_soldier£ %job_soldier% 岗位替换为£job_soldier£ %job_mercenary% 岗位，增加£mod_country_naval_cap_add£ §Y%MOD_COUNTRY_NAVAL_CAP_ADD%§!，生成£defense_army£ §Y防御部队§!并产出 £mod_trade_value_add£ %TRADE_VALUE%"
- swap_type:=>- trigger:=>- host_has_dlc:   Overlord
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "干涉主义"
- -  "军国主义"

- text:    "是一定程度的§Y%ethic_fanatic_militarist%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   10
- 修正:=>- - 因子:   2.5
- - 拥有思潮:    "军国主义"
- 修正:=>- - armies_upkeep_mult:   0.05
- - ARMY_STARTING_EXPERIENCE_ADD:   200
- - SHIP_STARTING_EXPERIENCE_ADD:   200
- - job_mercenary_add:   3
- - ships_upkeep_mult:   0.05
- leader_background_job_weight:=>- mercenary:   100
## <span title=civic_liberty_of_libido style="border-bottom:1px dotted"> "欲望自由"</span>
- 描述:    "—未采纳这个国民文化的国家对该文明的§Y评价§!§R-40§!，而同样采纳了这个国民文化的国家对该文明的§Y评价§!§G+40§!\n—允许开设§Y%has_branch_office%§!的国家能够建造特殊的%BRANCH_OFFICE_BUILDINGS%：§Y%building_alien_custom_street%§!\n—采纳%ap_engineered_evolution%飞升天赋后，%allow_crossbreeding%§H（可以在开局设置中开关这一选项）§!"
- swap_type:=>- trigger:=>- has_country_flag:   synthetic_empire
- 需求:=>- 思潮:=>- value:    "自由主义"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   5
- 修正:=>- - pop_growth_speed:   0.25
- - biological_pop_happiness:   0.15
- - lithoid_pop_happiness:   0.1
## <span title=civic_parliamentary_system_corporate style="border-bottom:1px dotted"> "民主制"</span>
- 随机权重:=>- 基础:   1
- 修正:=>- - 因子:   15
- - 拥有思潮:    "个人主义"
- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- 修正:=>- - country_unity_produces_mult:   0.25
- - pop_factions_produces_mult:   0.33
- - pop_growth_from_immigration:   0.25
- - country_base_influence_produces_add:   0.5
## <span title=civic_hive_strength_of_legions style="border-bottom:1px dotted">civic_hive_strength_of_legions</span>
- ai_weight:=>- 基础:   @ai_civic_default_base_weight
- 修正:=>- - 因子:   @ai_civic_personality_match_factor
- - OR:=>- has_ai_personality:   devouring_swarm
- 随机权重:=>- 基础:   5
- 前置条件:=>- 政体:=>- value:   auth_hive_mind
- 修正:=>- - army_damage_mult:   0.2
- - councilor_gestalt_regulatory_exp_gain:   @gestalt_civic_node_xp_rate
- - army_starting_experience_add:   250
- - armies_upkeep_mult:   -0.2
- - commander_initial_skill:   2
## <span title=civic_echo_corporate style="border-bottom:1px dotted"> "%civic_echo%"</span>
- 描述:    "—每个£mod_planet_jobs_robotic_produces_mult£ 机器人口额外产出%r_unity%与%r_trade_value%。\n—与其他文明签订外交协议后，研究花费§G-50%§!。"
- swap_type:=>- trigger:=>- any_country:=>- OR:=>- has_research_agreement:   root
- has_diplo_migration_treaty:   root
- has_communications:   root
- is_in_federation_with:   root
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "竞争主义"
- -  "个人主义"

- text:    "是一定程度的§Y%ethic_fanatic_capitalism%§!"
- 前置条件:=>- species_archetype:=>- value:   MACHINE
- ai_weight:=>- 基础:   @ai_civic_default_base_weight
- 随机权重:=>- 基础:   @civic_default_random_weight
- 修正:=>- - planet_researchers_engineering_research_produces_add:   -2
- - planet_researchers_society_research_produces_add:   -2
- - planet_researchers_physics_research_produces_add:   -2
## <span title=civic_commercial_entertainment style="border-bottom:1px dotted"> "商业化娱乐"</span>
- 描述:    "—£job_entertainer£ %job_entertainer_plural%额外产出§Y2§!£trade_value£ §Y%TRADE_VALUE%§!，但提供的£mod_planet_amenities_add£ %PLANET_AMENITIES_TITLE%§R-2§!并额外消耗§Y1§!£unity£ %unity%"
- swap_type:=>- 描述:    "—£job_duelist£ %job_duelist_plural%额外产出§Y2§!£trade_value£ §Y%TRADE_VALUE%§!，但提供的£mod_planet_amenities_add£ %PLANET_AMENITIES_TITLE%§R-2§!并额外消耗§Y1§!£unity£ %unity%"
- name:    "商业化娱乐"
- trigger:=>- is_duelist_country:   yes
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "竞争主义"
- -  "个人主义"

- text:    "是一定程度的§Y%ethic_fanatic_capitalism%§!"
- hide_modifiers:   yes
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - planet_entertainers_unity_upkeep_add:   1
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   5
- - 拥有思潮:    "个人主义"
## <span title=civic_franchising style="border-bottom:1px dotted">civic_franchising</span>
- 描述:   civic_tooltip_franchising_effects
- swap_type:=>- 描述:   civic_tooltip_franchising_effects
- trigger:=>- host_has_dlc:   Overlord
- 需求:=>- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- 修正:=>- - divided_patrongage_max_subjects:   2
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   5
- - 拥有思潮:    "崇外主义"
## <span title=civic_environmentalist style="border-bottom:1px dotted"> "环保政策"</span>
- 描述:    "—可以建造£building£ §Y%building_ranger_lodge%§!建筑，能够根据£blocker£ §Y星球自然障碍§!的数量添加£job_ranger£ §Y%job_ranger%§!岗位并提供额外£housing£ §Y住房§!\n—£job_ranger£ §Y%job_ranger_plural%§!产出£society£ §Y社会学研究§!以及%r_amenities%"
- 需求:=>- 思潮:=>- NOR:=>- value:    "个人主义"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   5
- - 拥有思潮:    "道德主义"
- 修正:=>- - job_environmental_pollution_caused_mult:   -0.15
- - planet_pops_consumer_goods_upkeep_mult:   -0.2
- - planet_max_buildings_add:   -1
- - planet_building_refund_mult:   0.15
- leader_background_job_weight:=>- ranger:   100
## <span title=civic_crusader_spirit style="border-bottom:1px dotted"> "十字军之魂"</span>
- 描述:    "—£building£§Y寺庙§!建筑额外提供£job_templar£ §Y%job_templar%§!岗位（结合§Y神权政治§!或§Y教权主义§!主题的国民理念可以让他们更强大）\n—£building£§Y祭祀之殿§!建筑额外提供£job_death_knight£ §Y%job_death_knight%§!岗位 \n—可以使用 £unity£ 凝聚力招募§H圣战者§!陆军，他们脆弱但攻击力强且士气高昂。\n—允许使用特殊凝聚力野望——§Y神圣远征§!\n—§Y%commander_plural_with_icon%§!初始拥有§Y%leader_trait_crusader%§!特质\n—仅限使用§Y解放战争§!政策"
- 需求:=>- 思潮:=>- value:    "教权主义"
- OR:=>- value:
- -  "干涉主义"
- -  "军国主义"
- -  "精英主义"
- -  "权威主义"

- text:   civic_tooltip_authoritarian_or_militarist
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   20
- 修正:=>- - 因子:   3
- - 拥有思潮:    "排外主义"
- 修正:=>- - army_attack_morale_mult:   0.15
- - rivalries_influence_produces_mult:   0.15
- - army_attack_damage_mult:   0.2
- - army_attack_health_mult:   0.25
- leader_background_job_weight:=>- templar:   100
- death_knight:   100
## <span title=civic_inwards_perfection style="border-bottom:1px dotted"> "内圣之道"</span>
- modification:=>- add:=>- has_tradition:    "未来传统完成"
- has_technology:   tech_ascension_theory
- 描述:    "—不能§Y宣布宿敌§!\n—不能签订§Y防御条约§!\n—不能签订§Y移民协议§!\n—不能签订§Y研究协议§!\n—不能签订§Y商业协议§!\n—不能§Y保障独立§!\n—不能加入§Y联邦§!\n—不能§Y渗透§!土著\n—不能使用§Y%liberation_wars%§!政策\n—建造§Y行星护盾生成器§!产出额外的 £unity£ 凝聚力\n—§Y边境政策§!默认§Y关闭§!"
- 需求:=>- 思潮:=>- value:    "排外主义"
- OR:=>- value:
- -  "和平主义"
- -  "道德主义"

- text:    "是一定程度的§Y%ethic_fanatic_pacifist%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   5
- 修正:=>- - leader_age:   10
- - pop_growth_speed:   0.25
- - pop_citizen_happiness:   0.15
- - envoys_add:   -1
- - country_unity_produces_mult:   0.25
- - country_edict_fund_add:   75
- - pop_government_ethic_attraction:   0.25
## <span title=civic_separation_of_powers style="border-bottom:1px dotted"> "三权分立"</span>
- 描述:    "—解锁§Y权力平衡§!法案，三种权力分别带来三种不同侧重的加成：\n——§G立法权§!：法令颁布与法令开销\n——§R司法权§!：遏制犯罪与稳定社会\n——§E行政权§!：国家治理与生产管理"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "宪政主义"
- -  "自由主义"

- text:    "是一定程度的§Y%ethic_fanatic_egalitarian%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   10
- 修正:=>- - 因子:   2.5
- - 拥有思潮:    "个人主义"
## <span title=civic_corporate_hedonism style="border-bottom:1px dotted">civic_corporate_hedonism</span>
- ai_playable:=>- host_has_dlc:   HumanoidsSpeciesPack
- 描述:   civic_tooltip_pleasure_seekers_effects
- playable:=>- host_has_dlc:   HumanoidsSpeciesPack
- 需求:=>- 思潮:=>- NOR:=>- value:
- -  "合作主义"
- -  "集体主义"

- text:    "不接受任何程度的§Y社会主义§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - planet_pops_consumer_goods_upkeep_mult:   0.1
- - trade_value_mult:   0.25
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   5
- - 拥有思潮:    "个人主义"
## <span title=civic_police_state style="border-bottom:1px dotted"> "警察国度"</span>
- 描述:    "—§Y警署§!和§Y审判厅§!建筑提供额外的 £job_enforcer£ §Y%job_enforcer_plural%§!岗位"
- 需求:=>- 思潮:=>- NOR:=>- value:    "自由主义"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- leader_background_job_weight:=>- enforcer:   100
- 修正:=>- - planet_telepaths_unity_produces_add:   1
- - planet_stability_add:   5
- - planet_enforcers_upkeep_mult:   0.15
- - planet_enforcers_unity_produces_add:   1
- - trade_value_mult:   -0.25
- - pop_ethic_egalitarian_attraction_mult:   -0.15
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   5
- - 拥有思潮:    "权威主义"
## <span title=civic_anglers style="border-bottom:1px dotted"> "渔夫"</span>
- modification:=>- add:=>- has_civic:   civic_machine_anglers
- playable:=>- has_aquatics:   yes
- alternate_civic_version:   civic_machine_anglers
- ai_playable:=>- has_aquatics:   yes
- 描述:   civic_tooltip_anglers_effects
- 需求:=>- origin:=>- NOR:=>- value:
- - origin_post_apocalyptic
- - origin_shattered_ring
- - origin_void_dwellers
- - origin_subterranean

- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   10
- - 拥有思潮:    "道德主义"
- traits:=>- trait:   trait_aquatic
- leader_background_job_weight:=>- angler:   50
## <span title=civic_military_industry_corporate style="border-bottom:1px dotted"> "战争工匠"</span>
- 随机权重:=>- 基础:   10
- 修正:=>- - 因子:   2.5
- - 拥有思潮:    "机械主义"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "技术主义"
- -  "机械主义"

- text:    "是一定程度的§Y%ethic_fanatic_materialist%§!"
- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- 修正:=>- - ship_armor_mult:   0.2
- - ship_weapon_damage:   0.2
- - ship_weapon_range_mult:   0.2
- - category_propulsion_research_speed_mult:   0.33
- - starbase_shipyard_build_cost_mult:   0.15
## <span title=civic_transcendence style="border-bottom:1px dotted"> "§E§H超凡入圣§!§!"</span>
- modification:   no
- 描述:   civic_tooltip_transcendence_effects
- 需求:=>- civics:=>- NOT:=>- value:    "知识崇拜"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- hide_modifiers:   yes
- 修正:=>- - all_technology_research_speed:   0.1
- - num_tech_alternatives_add:   -999
- - planet_researchers_unity_produces_add:   6
- 随机权重:=>- 基础:   5
## <span title=civic_better_future style="border-bottom:1px dotted"> "热爱生活"</span>
- 描述:   civic_tooltip_better_future_effects
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "竞争主义"
- -  "个人主义"

- text:    "是一定程度的§Y%ethic_fanatic_capitalism%§!"
- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- 修正:=>- - planet_investment_produces_mult:   0.33
- - trade_invest_unity_produces_mult:   -0.5
- 随机权重:=>- 基础:   5
## <span title=civic_private_military_companies style="border-bottom:1px dotted">civic_private_military_companies</span>
- 描述:    "—§Y要塞§!和§Y堡垒§!建筑将£job_soldier£ %job_soldier% 岗位替换为£job_soldier£ %job_mercenary% 岗位，增加£mod_country_naval_cap_add£ §Y%MOD_COUNTRY_NAVAL_CAP_ADD%§!，生成£defense_army£ §Y防御部队§!并产出 £mod_trade_value_add£ %TRADE_VALUE%"
- swap_type:=>- trigger:=>- host_has_dlc:   Overlord
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "干涉主义"
- -  "军国主义"

- text:    "是一定程度的§Y%ethic_fanatic_militarist%§!"
- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- 随机权重:=>- 基础:   25
- 修正:=>- - army_damage_mult:   0.2
- - ARMY_STARTING_EXPERIENCE_ADD:   200
- - job_mercenary_add:   3
- - armies_upkeep_mult:   0.05
- leader_background_job_weight:=>- mercenary:   100
## <span title=civic_spy_agency_corporate style="border-bottom:1px dotted"> "商业情报"</span>
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   5
- - 拥有思潮:    "排外主义"
- 需求:=>- 思潮:=>- NOR:=>- value:    "崇外主义"
- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- 修正:=>- - ship_cloaking_detection_add:   2
- - add_base_country_intel:   30
- - intel_decryption_add:   2
- - espionage_operation_cost_mult:   -0.25
- - spy_network_daily_value_mult:   0.25
## <span title=civic_task_delegation_corporate style="border-bottom:1px dotted">civic_task_delegation_corporate</span>
- ai_playable:=>- host_has_dlc:   GalacticParagons
- playable:=>- host_has_dlc:   GalacticParagons
- 需求:=>- 思潮:=>- NOT:=>- value:    "自由主义"
- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- 随机权重:=>- 基础:   4
- 修正:=>- - leaders_upkeep_mult:   -0.2
- - country_leader_cap_add:   1
- - negative_traits_country:   -1
## <span title=civic_machine_soul_servant style="border-bottom:1px dotted"> "机械崇拜"</span>
- modification:=>- add:=>- has_tradition:    "未来传统完成"
- has_technology:   tech_ascension_theory
- 描述:    "—['concept_robots', £job_priest£ %job_machine_soul_plural%]§I%pops_with_icon%§!：8\n—母星：['concept_mecha_monastery',£building£ %building_mecha_monastery%]\n—%ADDITONAL_TECHNOLOGIES_STRING%\n——['concept_powered_exoskeletons', £engineering_research£ %tech_powered_exoskeletons%]\n%t%——['concept_robotic_workers', £engineering_research£ %tech_robotic_workers%]"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "精神主义"
- -  "教权主义"

- text:    "是一定程度的§Y%ethic_fanatic_spiritualist%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   10
- 修正:=>- - 因子:   0
- - NOT:=>- host_has_dlc:   SyntheticDawnStoryPack
- leader_background_job_weight:=>- techno_priest:   100
## <span title=civic_byzantine_bureaucracy style="border-bottom:1px dotted"> "繁复官僚"</span>
- 描述:   "%civic_tooltip_byzantine_bureaucracy_effects%\n—开始游戏时解锁§Y%tech_living_state%§!科技"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "精英主义"
- -  "权威主义"

- text:    "是一定程度的§Y%ethic_fanatic_authoritarian%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - job_bureaucrat_per_pop:   0.04
- - category_statecraft_research_speed_mult:   0.33
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   0
- - has_civic:   civic_empty_vagrant
- - NOR:=>- has_origin:   origin_ev_both_choosen
- has_civic:   civic_ev_planet_and_fleet
- has_ascension_perk:   ev_land_planets
## <span title=civic_hive_natural_design style="border-bottom:1px dotted">civic_hive_natural_design</span>
- modification:   no
- playable:=>- has_machine_age_dlc:   yes
- ai_playable:=>- has_machine_age_dlc:   yes
- 描述:    "—开始游戏时就能§G成为完美的生物体§!。\n—%AVAILABLE_BUILDINGS%['concept_hive_transcendental_retreat']"
- 需求:=>- origin:=>- NOT:=>- value:   origin_overtuned
- 前置条件:=>- 政体:=>- value:   auth_hive_mind
- 随机权重:=>- 基础:   @civic_rare_random_weight
- 修正:=>- - councilor_gestalt_growth_exp_gain:   @gestalt_civic_node_xp_rate
- - BIOLOGICAL_species_trait_picks_add:   15
- - BIOLOGICAL_species_trait_points_add:   5
- - planet_researchers_society_research_produces_add:   0.33
- traits:=>- trait:
- - trait_latent_psionic
- - trait_erudite
- - trait_fertile
- - trait_robust

- negative_description:   civic_hive_tooltip_natural_design_negative_effects
## <span title=civic_liberator style="border-bottom:1px dotted"> "解放者"</span>
- 随机权重:=>- 基础:   30
- 描述:    "—§Y保障独立§!和§Y互不侵犯条约§!不需要影响力维护\n—§Y革命者派系§!对§Y防御条约§!给予支持\n—开始游戏时解锁%continuous_revolution%政策\n—§Y轨道轰炸§!选项受限\n—仅限使用§Y解放战争§!政策"
- 需求:=>- civics:=>- NOR:=>- value:
- - 1 "征服者"
- -  "调停者"

- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - diplo_weight_naval_mult:   0.15
- - country_war_exhaustion_mult:   -0.25
- - country_power_projection_influence_produces_add:   1
- - country_trust_growth:   -0.33
## <span title=civic_heroic_tales style="border-bottom:1px dotted">civic_heroic_tales</span>
- ai_playable:=>- host_has_dlc:   GalacticParagons
- playable:=>- host_has_dlc:   GalacticParagons
- 需求:=>- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   4
- 修正:=>- - negative_traits_country:   -2
- - country_leader_cap_add:   1
## <span title=civic_learning_society_corporate style="border-bottom:1px dotted"> "科研激励制度"</span>
- 随机权重:=>- 基础:   25
- 描述:    "—§Y科学家§!初始拥有随机的§Y专精§!特质\n—§Y科学家§!有两倍的机会发现属于他们研究领域的技术"
- 需求:=>- 思潮:=>- value:    "机械主义"
- NOR:=>- value:
- -  "宪政主义"
- -  "自由主义"

- text:    "不接受任何程度的§Y自由主义§!"
- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- 修正:=>- - planet_jobs_produces_mult:   0.1
- - species_leader_exp_gain:   0.33
- - planet_pops_consumer_goods_upkeep_mult:   0.15
## <span title=civic_traffic_password style="border-bottom:1px dotted"> "流量密码"</span>
- 描述:   civic_tooltip_traffic_password_effects
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "竞争主义"
- -  "个人主义"

- text:    "是一定程度的§Y%ethic_fanatic_capitalism%§!"
- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- 随机权重:=>- 基础:   5
## <span title=civic_shadow_council_corporate style="border-bottom:1px dotted"> "有限责任公司"</span>
- 随机权重:=>- 基础:   10
- 修正:=>- - 因子:   2.5
- - is_authoritarian:   yes
- 需求:=>- civics:=>- NOT:=>- value:    "§H§Y家族企业§!§!"
- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- 修正:=>- - planet_jobs_ruler_produces_mult:   0.1
- - country_election_cost_mult:   -0.75
- - pop_cat_ruler_political_power:   1
## <span title=civic_idealistic_foundation_corporate style="border-bottom:1px dotted"> "企业文化"</span>
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   5
- - 拥有思潮:    "个人主义"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "宪政主义"
- -  "自由主义"

- text:    "是一定程度的§Y%ethic_fanatic_egalitarian%§!"
- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- 修正:=>- - planet_stability_add:   10
- - pop_job_trade_mult:   0.15
- - pop_ethic_egalitarian_attraction_mult:   0.1
## <span title=civic_machine_syntheticLove style="border-bottom:1px dotted"> "合成之爱"</span>
- 随机权重:=>- 基础:   5
- 需求:=>- civics:=>- value:   civic_machine_servitor
- 前置条件:=>- 政体:=>- OR:=>- value:
- - auth_machine_intelligence
- - auth_ancient_machine_intelligence

- 修正:=>- - councilor_gestalt_growth_exp_gain:   @gestalt_civic_node_xp_rate
- 描述:   1"允许特殊法令——§Y合成之爱§!\n—机械人口将会消耗额外的£food£ %food%\n—失业的子个体会自动转换为£job_breeding_drone£ §Y%job_breeding_drone_plural%§!，增加§Y%MOD_POP_GROWTH_SPEED%§!和£happiness£§Y生物人口幸福度§!，并产出少量£unity£ %unity%和£amenities£ %MOD_PLANET_AMENITIES_ADD%"
## <span title=civic_psionic_sovereign style="border-bottom:1px dotted">civic_psionic_sovereign</span>
- modification:   no
- 随机权重:=>- 基础:   0
- icon:   gfx/interface/icons/governments/civics/civic_psionic_sovereign.dds
- 前置条件:=>- civics:=>- value:   civic_psionic_sovereign
- 修正:=>- - pop_citizen_happiness:   0.1
- - planet_jobs_produces_mult:   0.15
- - country_government_civic_points_add:   2
- - pop_government_ethic_attraction:   1
## <span title=civic_honorary_curator style="border-bottom:1px dotted"> "荣誉策展人"</span>
- 随机权重:=>- 基础:   10
- 修正:=>- - 因子:   2.5
- - 拥有思潮:    "崇外主义"
- 描述:    "—提高§H非灭绝§!国家对你的评价\n—相邻的国家§G+10%§!%mod_country_unity_produces_mult%\n—§Y市场经济§!下, 无经济危机时, 提供§Y+0.1§!%economic_situation_improve%和§Y+40§!%economic_crisis_threshold%。"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "和平主义"
- -  "道德主义"

- text:    "是一定程度的§Y%ethic_fanatic_pacifist%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - add_base_country_intel:   20
- - diplo_weight_mult:   0.25
- - planet_jobs_specialist_produces_mult:   0.1
- - country_energy_produces_mult:   -0.1
## <span title=civic_machine_terminator style="border-bottom:1px dotted">civic_machine_terminator</span>
- modification:=>- add:=>- has_tradition:    "未来传统完成"
- has_technology:   tech_ascension_theory
- 描述:    "—起始首都是一颗§Y死寂星球§!\n—无法与其他有机物种展开§Y外交§!！\n—无法进入§Y泛星系贸易市场§!\n—对其他有机物种拥有§Y“净化”§!宣战理由\n—有机£pop£人口将总是会被§Y净化§!\n—净化有机£pop£ 人口将获得£unity£ £society£ £engineering£ £physics£ §Y凝聚力和研究点数§!\n—可以使用§Y%bombardment_armageddon%§!轰炸姿态"
- pc_nukedpossible:=>- civics:=>- NOR:=>- value:
- - "创世向导"
- - civic_corporate_guided_sapience
- - civic_hive_guided_sapience
- - civic_machine_guided_sapience

- text:   civic_tooltip_not_guided
- 前置条件:=>- 政体:=>- OR:=>- value:
- - auth_ancient_machine_intelligence
- - auth_machine_intelligence

- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   0
- - NOT:=>- host_has_dlc:   SyntheticDawnStoryPack
- 修正:=>- - starbase_shipyard_build_cost_mult:   -0.33
- - country_starbase_influence_cost_mult:   -0.33
- - councilor_gestalt_legion_exp_gain:   @gestalt_civic_node_xp_rate
- - ship_weapon_damage:   0.66
- - country_naval_cap_mult:   1.25
## <span title=civic_reanimated_armies style="border-bottom:1px dotted">"逝者军势"</span>
- modification:=>- add:=>- has_tradition:    "未来科技"
- 描述:   civic_tooltip_reanimated_armies_effects
- playable:=>- host_has_dlc:   NecroidsSpeciesPack
- 需求:=>- 思潮:=>- NOR:=>- value:
- -  "和平主义"
- -  "道德主义"

- text:    "不接受任何程度的§Y道德主义§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   15
- 修正:=>- - 因子:   5
- - has_origin:   origin_necrophage
- leader_background_job_weight:=>- necromancer:   100
## <span title=civic_triple_the_profit style="border-bottom:1px dotted"> "§E§H三倍利润§!§!"</span>
- 描述:    "—能够无视思潮与国策的限制进行剥削\n—开始游戏时解锁§Y%tech_artificial_moral_codes%§!科技\n—对其它所有帝国拥有§Y“%casus_belli_cb_despoliation%”§!宣战理由\n—%allow_raiding%\n—§Y奴隶§!人口额外产出§Y3§!£trade_value£ %TRADE_VALUE%\n—§Y市场经济§!下，即使处于经济危机时，%economic_factor_market%依旧会提供%economic_situation_improve%。\n—§Y市场经济§!下，无经济危机时，提供§Y+3.0§!%economic_situation_improve%和§Y+3.0§!%economic_crisis_accumulate%。"
- 需求:=>- 思潮:=>- value:    "个人主义"
- NOT:=>- value:    "道德主义"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - planet_jobs_slave_produces_mult:   0.5
- - pop_category_rulers_consumer_goods_upkeep_add:   3
- - pop_cat_slave_happiness:   -3
- - pop_cat_ruler_happiness:   3
- - pop_growth_speed_reduction:   0.33
- - trade_value_mult:   3
- - trade_value_reduction:   0.75
- custom_tooltip_with_modifiers:   civic_triple_the_profit_effects_additional
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   0
- - has_civic:   civic_empty_vagrant
- - NOR:=>- has_origin:   origin_ev_both_choosen
- has_civic:   civic_ev_planet_and_fleet
- has_ascension_perk:   ev_land_planets
## <span title=civic_relentless_industrialists style="border-bottom:1px dotted"> "无情工业化"</span>
- ai_playable:=>- has_toxoids:   yes
- 描述:    "—不能使用§Y加强环境监管§!政策\n—§Y企业家§!派系要求§Y减少环境监管§!政策\n—每§Y3§!个§H工业区划§!解锁§G2§!£building£§Y建筑槽位§!，轨道居住站除外。\n—§Y工业建筑§!额外提供岗位和贸易额，能够修建£building£ §Y%building_coordinated_fulfillment_center_1%§!，极大地增加£alloys£ §Y合金§!和£consumer_goods£ §Y消费品§!的产出，代价是减少£mod_pop_growth_speed£ §Y人口增长§!，同时还会逐渐将行星变为§Y死寂星球§!\n—§Y市场经济§!下, 无经济危机时, 提供§Y+0.1§!%economic_situation_improve%和§Y-40§!%economic_crisis_threshold%。"
- playable:=>- has_toxoids:   yes
- 需求:=>- 思潮:=>- value:    "机械主义"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   20
- 修正:=>- - planet_jobs_worker_produces_mult:   0.15
- - planet_building_build_speed_mult:   0.50
- - POP_ENVIRONMENT_TOLERANCE:   -0.15
## <span title=civic_naval_contractors style="border-bottom:1px dotted">civic_naval_contractors</span>
- 随机权重:=>- 基础:   25
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "干涉主义"
- -  "军国主义"

- text:    "是一定程度的§Y%ethic_fanatic_militarist%§!"
- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- 修正:=>- - country_naval_cap_mult:   0.15
- - job_commandante_add:   2
- - command_limit_add:   40
- swap_type:=>- trigger:=>- host_has_dlc:   Overlord
## <span title=civic_socialistic style="border-bottom:1px dotted"> "§H§Y先锋队政治§!§!"</span>
- 描述:    "—£building£ §Y首都建筑§!会替换部分 £job_politician£ §Y%job_politician%§!岗位为 £job_grassroot_cadre£ §Y%job_grassroot_cadre_plural%§!。\n—£job_labour_hero£ §Y%job_labour_hero%§!额外产出§Y0.5§!£unity£ 凝聚力。\n—§Y%pop_cat_worker%§!阶级额外产出§Y0.25§!£unity£ 凝聚力，并额外§G+1%§!%MOD_PLANET_BUILDING_BUILD_SPEED_MULT%，但额外消耗§Y0.15§!£consumer_goods£ 消费品。\n—§Y领袖§!有§Y20%§!几率初始自带额外的正面及负面特质各一个。"
- swap_type:=>- 描述:   civic_tooltip_communist_society_effects
- trigger:=>- is_egalitarian:   yes
- has_tradition:    "未来社会"
- is_xenophobe:   no
- is_democratic_country:   yes
- 拥有思潮:    "集体主义"
- has_technology:   tech_ascension_theory
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "合作主义"
- -  "集体主义"

- text:    "是一定程度的§Y%ethic_fanatic_socialism%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- leader_background_job_weight:=>- "grassroot_cadre":   50
- "labour_hero":   25
- 随机权重:=>- 基础:   60
- 修正:=>- - 因子:   0
- - has_civic:   civic_empty_vagrant
- - NOR:=>- has_origin:   origin_ev_both_choosen
- has_civic:   civic_ev_planet_and_fleet
- has_ascension_perk:   ev_land_planets
- 修正:=>- - leaders_upkeep_mult:   0.15
- - councilor_skill_add:   2
- - council_agenda_finishing_effect_duration_mult:   0.15
- - pop_ethic_socialism_attraction_mult:   0.25
## <span title=civic_hive_biochemical_warrior style="border-bottom:1px dotted"> "%civic_biochemical_warrior%"</span>
- 描述:    "—%javorian_pox_desc%\n—开始游戏时解锁§Y%tech_dangerous_wildlife%§!与§Y%tech_dense_jungle%§!科技"
- 修正:=>- - pop_environment_tolerance:   -0.1
- - army_defense_damage_mult:   0.25
- - planet_carry_cap_add:   -10
- 前置条件:=>- OR:=>- 政体:=>- value:   auth_hive_mind
- 随机权重:=>- 基础:   5
## <span title=civic_glory_and_dream style="border-bottom:1px dotted"> "§H§Y光荣与梦想§!§!"</span>
- 描述:    "—£building£ §Y首都建筑§!会替换部分 £job_politician£ §Y%job_politician%§!岗位为 £job_mogul£ §Y%job_mogul%§!岗位\n—可以对其他国家使用§Y新秩序§!宣战借口\n—§H未被奴役的主体种族§!将增加§Y%mod_planet_jobs_slave_produces_mult%§!\n—拥有§H%citizenship_full%§!的种族可采用§Y%living_standard_good%§!生活标准\n—其他种族只能成为§H%citizenship_slavery%§!或§H%citizenship_purge%§!"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "竞争主义"
- -  "个人主义"

- text:    "是一定程度的§Y%ethic_fanatic_capitalism%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - pop_ethic_xenophobe_attraction_mult:   0.2
- - country_starbase_influence_cost_mult:   -0.25
- - pop_citizen_happiness:   0.1
- - trade_value_mult:   -0.15
- - pop_ethic_capitalism_attraction_mult:   0.2
- 随机权重:=>- 基础:   75
- 修正:=>- - 因子:   0
- - has_civic:   civic_empty_vagrant
- - NOR:=>- has_origin:   origin_ev_both_choosen
- has_civic:   civic_ev_planet_and_fleet
- has_ascension_perk:   ev_land_planets
## <span title=civic_criminal_heritage style="border-bottom:1px dotted">civic_criminal_heritage</span>
- modification:=>- add:=>- has_tradition:    "未来传统完成"
- has_technology:   tech_ascension_theory
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "干涉主义"
- -  "军国主义"

- text:    "是一定程度的§Y%ethic_fanatic_militarist%§!"
- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- 随机权重:=>- 基础:   1
- 修正:=>- - 因子:   25
- - 拥有思潮:    "个人主义"
- 修正:=>- 描述:   civic_tooltip_criminal_heritage_effects
## <span title=civic_machine_servitor style="border-bottom:1px dotted">civic_machine_servitor</span>
- modification:=>- add:=>- has_tradition:    "未来传统完成"
- has_technology:   tech_ascension_theory
- 描述:   civic_tooltip_machine_servitor_effects
- has_secondary_species:=>- title:   civic_machine_servitor_secondary_species
- 需求:=>- civics:=>- NOR:=>- value:
- - civic_machine_terminator
- - civic_machine_assimilator
- -  "赤诚解放者"
- -  "金融投资网络"

- 前置条件:=>- 政体:=>- value:   auth_machine_intelligence
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   0
- - has_global_flag:   game_started
- 修正:=>- - councilor_gestalt_regulatory_exp_gain:   @gestalt_civic_node_xp_rate
## <span title=civic_ruthless_competition style="border-bottom:1px dotted">civic_ruthless_competition</span>
- 需求:=>- 思潮:=>- NOR:=>- value:
- -  "合作主义"
- -  "集体主义"

- text:    "不接受任何程度的§Y社会主义§!"
- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- 修正:=>- - species_leader_exp_gain:   5
- - leader_lifespan_add:   -20
- - planet_jobs_produces_mult:   0.33
- - pop_growth_speed_reduction:   0.33
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   3
- - 拥有思潮:    "个人主义"
## <span title=civic_shadow_council style="border-bottom:1px dotted">civic_shadow_council</span>
- 随机权重:=>- 基础:   10
- 修正:=>- - 因子:   2.5
- - is_authoritarian:   yes
- 需求:=>- 政体:=>- OR:=>- value:
- -  "间接民主"
- -  "寡头政治"
- -  "选举专制"

- text:   civic_tooltip_dem_oli_dic
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - planet_jobs_ruler_produces_mult:   0.1
- - country_election_cost_mult:   -0.75
- - pop_cat_ruler_political_power:   1
## <span title=civic_machine_extremely_efficient_storage style="border-bottom:1px dotted"> "%civic_extremely_efficient_storage%"</span>
- 描述:    "—§Y%building_resource_silo%§!行星建筑额外§G+5000§!%MOD_COUNTRY_RESOURCE_MAX_ADD%，提高星球%MOD_PLANET_AMENITIES_MULT%并§G+1§!£job_warrior_drone£ %job_warrior_drone_plural%岗位\n—§Y%building_resource_silo%§!恒星基地建筑额外§G+5000§!%MOD_COUNTRY_RESOURCE_MAX_ADD%，并§G+1§!£unity£ %unity%\n—£building£§Y首都建筑§!提供的%MOD_COUNTRY_RESOURCE_MAX_ADD%翻倍"
- alternate_civic_version:    "极效仓储"
- 前置条件:=>- 政体:=>- value:   auth_machine_intelligence
- 修正:=>- - country_resource_max_minor_artifacts_add:   2500
- - country_resource_max_astral_threads_add:   250
- 随机权重:=>- 基础:   5
## <span title=civic_dimensional_worship style="border-bottom:1px dotted">"维度崇拜"</span>
- ai_playable:=>- has_astral_planes_dlc:   yes
- 描述:   civic_dimensional_worship_effects
- playable:=>- has_astral_planes_dlc:   yes
- 需求:=>- civics:=>- NOT:=>- value:    "死亡教团"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - country_astral_threads_produces_mult:   0.25
- custom_tooltip_with_modifiers:   civic_dimensional_worship_effects_additional
## <span title=civic_free_haven style="border-bottom:1px dotted">civic_free_haven</span>
- 随机权重:=>- 基础:   10
- 修正:=>- - 因子:   2.5
- - 拥有思潮:    "自由主义"
- 描述:    "—§Y移民条约§!产生§G15§!£physics£ £society£ £engineering£ §Y研究点§!与§G30§! %r_unity%\n"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "多元主义"
- -  "崇外主义"

- text:    "是一定程度的§Y%ethic_fanatic_xenophile%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - pop_growth_from_immigration:   0.15
- - planet_immigration_pull_mult:   0.5
- - pop_ethic_xenophobe_attraction_mult:   -0.5
## <span title=civic_liberation_theology style="border-bottom:1px dotted"> "解放神学"</span>
- 随机权重:=>- 基础:   15
- 修正:=>- - 因子:   5
- - 拥有思潮:    "自由主义"
- 描述:    "—£job_priest£ §Y%job_priest_plural%§!能够提高§Y%pop_cat_worker%§!阶级的£happiness£§Y幸福度§!，同时额外产出少量的 £minerals£ 矿物，£food£ 食物和 £unity£ 凝聚力\n—§Y%pop_cat_worker%§!阶级额外产出§Y0.25§!£unity£ 凝聚力，并额外消耗§Y0.15§!£consumer_goods£ 消费品\n—§Y宗教派系§!会因§Y社会平等§!或§Y乌托邦§!生活标准感到愉悦"
- 需求:=>- 思潮:=>- value:    "集体主义"
- OR:=>- value:
- -  "精神主义"
- -  "教权主义"

- text:    "是一定程度的§Y%ethic_fanatic_spiritualist%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - planet_pops_organics_minerals_upkeep_mult:   0.15
- - planet_jobs_worker_produces_mult:   0.25
- - country_unity_produces_mult:   0.2
- - planet_pops_organics_food_upkeep_mult:   0.15
- - pop_ethic_socialism_attraction_mult:   0.15
## <span title=civic_conciliatory style="border-bottom:1px dotted"> "调和主义"</span>
- 描述:    "—§H激进思潮§!的修正效果将被抵消。"
- 需求:=>- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   5
## <span title=civic_the_land_of_smiles style="border-bottom:1px dotted"> "微笑企业"</span>
- 需求:=>- 思潮:=>- NOR:=>- value:
- -  "崇外主义"
- -  "军国主义"

- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- 修正:=>- - intel_encryption_add:   3
- - ship_cloaking_strength_add:   1
- - country_election_cost_mult:   -0.75
- - planet_amenities_mult:   -0.25
- 随机权重:=>- 基础:   10
- 修正:=>- - 因子:   2.5
- - is_pacifist:   yes
## <span title=civic_agrarian_idyll style="border-bottom:1px dotted">1 "田园牧歌"</span>
- 描述:    "—£job_farmer£ §Y%job_farmer_plural%§!同时产出§G3§! £amenities£ 舒适度和§Y2§! £trade_value£ 贸易额"
- 需求:=>- civics:=>- NOR:=>- value:
- -  "无情工业化"
- - civic_mining_guilds

- leader_background_job_weight:=>- "farmer":   50
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - farming_district_housing_add:   1
- - generator_district_housing_add:   1
- - farming_district_buildings_add:   0.34
- - planet_farmers_food_produces_add:   1
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   0.2
- - has_civic:    "§H§Y先锋队政治§!§!"
## <span title=civic_corporate_dominion style="border-bottom:1px dotted">1 "和平商人"</span>
- 随机权重:=>- 基础:   10
- 修正:=>- - 因子:   2.5
- - 拥有思潮:    "道德主义"
- 描述:    "—§Y外星贸易公司§!恒星基地建筑产出额外§Y4§! £trade_value£ %TRADE_VALUE%，§Y贸易中心§!模块§Y%MOD_STARBASE_TRADE_COLLECTION_RANGE_ADD%§!提高§G+1§!\n—£job_merchant£ %job_merchant_plural%、£job_manager£ %job_manager_plural%、和£job_trader£ %job_trader_plural%额外产出§Y1§! £unity£ 凝聚力\n—开始游戏时解锁§Y%tech_space_trading%§!科技"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "和平主义"
- -  "道德主义"

- text:    "是一定程度的§Y%ethic_fanatic_pacifist%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - job_merchant_add:   2
- - country_resource_max_add:   10000
- - country_starbase_capacity_add:   5
- - army_morale:   -0.15
## <span title=civic_machine_warbots style="border-bottom:1px dotted">civic_machine_warbots</span>
- 随机权重:=>- 基础:   5
- 前置条件:=>- 政体:=>- OR:=>- value:
- - auth_ancient_machine_intelligence
- - auth_machine_intelligence

- 修正:=>- - army_damage_mult:   0.25
- - armies_upkeep_mult:   -0.25
- - councilor_gestalt_legion_exp_gain:   @gestalt_civic_node_xp_rate
- - commander_initial_skill:   2
## <span title=civic_keepers_harmony style="border-bottom:1px dotted"> "自然卫士"</span>
- 随机权重:=>- 基础:   15
- 修正:=>- - 因子:   5
- - 拥有思潮:    "道德主义"
- 描述:    "—可以建造£building£ §Y%building_ranger_lodge%§!建筑，能够根据£blocker£ §Y星球自然障碍§!的数量添加£job_druid£ §Y%job_druid%§!岗位并提高%MOD_POP_CITIZEN_HAPPINESS%\n—建造§Y乐土园§!提供额外 £housing£ 住房，并提高 £unity£ 凝聚力产出\n—拥有特殊星球决策，可根除星球的异常，例如§Y危险野生动物§!、§Y苍茫大地§!、§Y变幻莫测的天气§!、§Y狂野之风§!、§Y生态受损§!、§Y辐照天地§!、§Y废土辐射§!\n—§Y采矿区划§!降低§R1§! £amenities£ 舒适度\n—不能使用§Y减少环境监管§!政策"
- 需求:=>- 思潮:=>- NOT:=>- value:    "个人主义"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - planet_pops_consumer_goods_upkeep_mult:   -0.2
- - planet_pops_organics_food_upkeep_mult:   -0.1
- - pop_amenities_usage_mult:   -0.2
- - deposit_blockers_natural_unity_produces_add:   5
- - job_environmental_pollution_caused_mult:   -0.30
- - planet_pops_minerals_upkeep_mult:   -0.1
- - planet_max_districts_add:   -1
## <span title=civic_hero_family style="border-bottom:1px dotted"> "英雄家庭"</span>
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "合作主义"
- -  "集体主义"

- text:    "是一定程度的§Y%ethic_fanatic_socialism%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - pop_growth_speed:   0.3
- - planet_pops_consumer_goods_upkeep_mult:   0.15
- 随机权重:=>- 基础:   10
- 修正:=>- - 因子:   2.5
- - 拥有思潮:    "集体主义"
## <span title=civic_machine_predictive_analysis style="border-bottom:1px dotted">civic_machine_predictive_analysis</span>
- 随机权重:=>- 基础:   5
- 描述:   civic_tooltip_machine_predictive_analysis_effects
- 前置条件:=>- 政体:=>- value:   auth_machine_intelligence
- 修正:=>- - councilor_gestalt_cognitive_exp_gain:   @gestalt_civic_node_xp_rate
- - num_tech_alternatives_add:   2
- - intel_decryption_add:   1
## <span title=civic_free_expeditionary_force style="border-bottom:1px dotted"> "自由远征军"</span>
- 描述:    "—能够使用§B“为了人杈”§!战争理由\n—§R不能与战争中的国家签订§Y商业条约§!§!"
- 需求:=>- civics:=>- value:    "民主制"
- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- 修正:=>- - pop_growth_from_immigration:   0.15
- - country_power_projection_influence_produces_add:   1
- - country_claim_influence_cost_mult:   -0.15
- - planet_stability_add:   -5
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   0
- - 拥有思潮:    "自由主义"
## <span title=civic_ultravisionary_socialism style="border-bottom:1px dotted"> "远视主义"</span>
- 随机权重:=>- 基础:   25
- 描述:    "—£building£ §Y研究建筑§!额外提供£job£ 岗位并提高£happiness£ %MOD_POP_CITIZEN_HAPPINESS%。\n—£job_labour_hero£ §Y%job_labour_hero_plural%§!的岗位产出替换为£physics£ £society£ £engineering£ 研究点数。\n—解锁['concept_unique_technology']：%civic_OGAS%"
- 需求:=>- 思潮:=>- value:    "集体主义"
- OR:=>- value:
- -  "技术主义"
- -  "机械主义"

- text:    "是一定程度的§Y%ethic_fanatic_materialist%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - planet_researchers_physics_research_produces_add:   1.5
- - planet_researchers_engineering_research_produces_add:   1.5
- - planet_researchers_consumer_goods_upkeep_add:   1
- - planet_researchers_society_research_produces_add:   1.5
- - planet_researchers_energy_upkeep_add:   1
## <span title=civic_star_settlers style="border-bottom:1px dotted"> "星之开拓者"</span>
- 随机权重:=>- 基础:   15
- 修正:=>- - 因子:   10
- - is_eager_explorer_empire:   yes
- 描述:    "—£job_colonist£ §Y%job_colonist_plural%§!同时产出 §Y5§! £unity£ 凝聚力\n—开始游戏时解锁§Y星际野望§!科技"
- 需求:=>- 思潮:=>- NOR:=>- value:
- -  "单一主义"
- -  "排外主义"

- text:    "不接受任何程度的§Y排外主义§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - colony_start_num_pops_add:   1
- - category_new_worlds_research_speed_mult:   0.2
- - country_starbase_influence_cost_mult:   -0.33
- - category_voidcraft_research_speed_mult:   0.1
## <span title=civic_hyperspace_specialty style="border-bottom:1px dotted">"速度与激情"</span>
- ai_playable:=>- has_astral_planes_dlc:   yes
- 描述:   civic_hyperspace_specialty_effects
- playable:=>- has_astral_planes_dlc:   yes
- 需求:=>- civics:=>- NOR:=>- value:
- - civic_eager_explorers
- -  "私人航空集团"
- - civic_hive_stargazers
- - civic_machine_exploration_protocol

- text:   civic_tooltip_not_eager_explorers
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - ship_speed_mult:   0.15
- - planet_sensor_range_add:   2
- - category_propulsion_research_speed_mult:   0.15
## <span title=civic_forum_friends_corporate style="border-bottom:1px dotted"> "%civic_forum_friends%"</span>
- modification:=>- add:=>- has_civic:    "论坛水友"
- 描述:    "—游戏开始时将有§Y1~5个§!随机文明获得这一国民理念，而这些文明将会互相取得通讯并组建一个['concept_common_ground_federation']。\n—开始游戏时解锁§Y%tech_xeno_linguistics%§!科技"
- 需求:=>- 思潮:=>- NOR:=>- value:
- -  "单一主义"
- -  "排外主义"

- text:    "不接受任何程度的§Y排外主义§!"
- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- alternate_civic_version:    "论坛水友"
- 随机权重:=>- 基础:   0
## <span title=civic_fanatic_purifiers style="border-bottom:1px dotted"> "§E§H种族洁癖§!§!"</span>
- 描述:    "—无法与其他物种展开§Y外交§!！\n—无法进入§Y泛星系贸易市场§!\n—对其他物种拥有§Y“净化”§!宣战理由\n—§Y异种人口§!将总是会被净化\n—净化异种£pop£ 人口将获得£unity£ £society£ £engineering£ £physics£ §Y凝聚力和研究点数§!\n—可以使用§Y%bombardment_armageddon%§!轰炸姿态\n—搭配§H教权主义§!可以使用 £unity£ 凝聚力招募§H圣战者§!陆军，他们脆弱但攻击力强且士气高昂。"
- playable:=>- host_has_dlc:   Utopia
- 需求:=>- 思潮:=>- value:    "排外主义"
- NOR:=>- value:
- -  "和平主义"
- -  "道德主义"

- text:    "不接受任何程度的§Y道德主义§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   0
- - NOT:=>- host_has_dlc:   Utopia
- 修正:=>- - ship_fire_rate_mult:   0.66
- - army_damage_mult:   0.66
- - pop_ethic_militarist_attraction_mult:   1
- - starbase_shipyard_build_cost_mult:   -0.25
- - country_naval_cap_mult:   1
- - pop_ethic_xenophobe_attraction_mult:   1
- - country_starbase_influence_cost_mult:   -0.2
## <span title=civic_machine_guided_sapience style="border-bottom:1px dotted">civic_machine_guided_sapience</span>
- modification:=>- add:=>- has_tradition:    "未来科技"
- has_technology:   tech_epigenetic_triggers
- playable:=>- has_machine_age_dlc:   yes
- alternate_civic_version:   "创世向导"
- ai_playable:=>- has_machine_age_dlc:   yes
- 描述:   civic_tooltip_guided_sapience_effects
- 需求:=>- origin:=>- NOT:=>- value:   origin_life_seeded
- 前置条件:=>- 政体:=>- value:   auth_machine_intelligence
- NOR:=>- value:
- - auth_corporate
- - auth_hive_mind

- 随机权重:=>- 基础:   @civic_rare_random_weight
- 修正:=>- - terraforming_cost_mult:   -0.25
- - councilor_gestalt_cognitive_exp_gain:   @gestalt_civic_node_xp_rate
- - terraform_speed_mult:   0.25
- negative_description:   civic_tooltip_guided_sapience_gestalt_negative_effects
## <span title=civic_welfare_state style="border-bottom:1px dotted"> "福利国家"</span>
- 描述:    "—§Y城市区划§!提供§G+1§! £housing£ 住房\n—£job_politician£ §Y%job_politician%§!岗位提供§G+2§! £amenities£ 舒适度\n—每个§Y矿业§!，§Y农业§!和§Y发电§!区划提供§G+1§!住房\n—不能使用§Y私人医疗§!或§Y私立教育§!政策\n—必须使用§Y社会福利§!生活标准\n—§Y市场经济§!下，无经济危机时，提供§Y-0.1§!%economic_situation_improve%和§Y-10%§!%economic_crisis_accumulate%。"
- swap_type:=>- trigger:=>- has_country_flag:   synthetic_empire
- 需求:=>- 思潮:=>- NOR:=>- value:    "权威主义"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   0.1
- - OR:=>- has_civic:
- -  "§H§Y先锋队政治§!§!"
- - 1 "§H§Y全息之眼§!§!"

- has_valid_civic:    "§H§Y工团主义§!§!"
- 修正:=>- - pop_family_structure_growth_mult:   -0.25
- - pop_growth_speed:   0.2
- - pop_category_workers_consumer_goods_upkeep_add:   0.5
- - planet_pops_unemployed_consumer_goods_upkeep_add:   1
- - planet_structures_upkeep_mult:   0.2
## <span title=civic_efficient_bureaucracy style="border-bottom:1px dotted">civic_efficient_bureaucracy</span>
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   2
- - is_authoritarian:   yes
- 需求:=>- civics:=>- NOR:=>- value:
- -  "民主廉政"
- -  "繁复官僚"
- - 1 "§H§Y无政府主义§!§!"

- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - decisions_cost_mult:   -0.1
- - starbases_upkeep_mult:   -0.1
- - country_admin_cap_mult:   0.25
- - planet_bureaucrats_upkeep_mult:   0.1
## <span title=civic_cultural_thief style="border-bottom:1px dotted"> "上周古国"</span>
- 描述:    "—£job_artisan£ %job_artisan_specialist_plural%额外消耗§Y1§!£minerals£ %minerals%，产出§Y0.25§!£minor_artifacts£ %fake_artifacts%\n—£job_artisan£ %job_artisan_plural%额外消耗§Y0.5§!£minerals£ %minerals%，产出§Y0.1§!£minor_artifacts£ %fake_artifacts%\n—允许特殊法令——§Y%edict_since_ancient_times%§!，大幅度减少领土宣称的花费"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "单一主义"
- -  "排外主义"

- text:    "是一定程度的§Y%ethic_fanatic_xenophobe%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   0
## <span title=civic_idyllic_bloom style="border-bottom:1px dotted">"田园绽放"</span>
- modification:=>- add:=>- has_tradition:    "未来科技"
- ai_playable:=>- host_has_dlc:   PlantoidsSpeciesPack
- playable:=>- host_has_dlc:   PlantoidsSpeciesPack
- 描述:   civic_tooltip_idyllic_bloom_effects
- 需求:=>- civics:=>- NOR:=>- value:    "无情工业化"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   10
- 修正:=>- - 因子:   5
- - 拥有思潮:    "道德主义"
## <span title=civic_individual_machine_replication_corporate style="border-bottom:1px dotted"> "%civic_individual_machine_replication%"</span>
- ai_weight:=>- 基础:   @ai_civic_default_base_weight
- 随机权重:=>- 基础:   @civic_default_random_weight
- 前置条件:=>- species_archetype:=>- value:   MACHINE
- 修正:=>- - official_exp_gain:   0.15
- - planet_pop_assembly_mult:   0.25
## <span title=civic_in_perfect style="border-bottom:1px dotted"> "部落文化"</span>
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   5
- - 拥有思潮:    "集体主义"
- swap_type:=>- trigger:=>- has_origin:   origin_FBCIV_default
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "合作主义"
- -  "集体主义"

- text:    "是一定程度的§Y%ethic_fanatic_socialism%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - rivalries_influence_produces_mult:   0.2
- - citizen_pop_same_species_class_happiness:   0.025
- - pop_housing_usage_mult:   -0.15
- - country_trust_growth:   -0.5
## <span title=civic_civil_rights_gun_grant style="border-bottom:1px dotted"> "武斗"</span>
- 随机权重:=>- 基础:   10
- 修正:=>- - 因子:   5
- - 拥有思潮:    "自由主义"
- 描述:    "—£job_foundry£ %job_foundry_plural%能够增加%MOD_ARMY_STARTING_EXPERIENCE_ADD%"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "干涉主义"
- -  "军国主义"

- text:    "是一定程度的§Y%ethic_fanatic_militarist%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - pop_cat_specialist_political_power:   2
- - pop_cat_worker_political_power:   1
## <span title=civic_firing_torch style="border-bottom:1px dotted"> "§E§H星星之火§!§!"</span>
- 描述:    "—当星球人口数量小于§Y50§!时，每个人口§G+2%§!%MOD_PLANET_BUILDING_BUILD_SPEED_MULT%。\n—国家灭亡时，如果该理念仍然生效，则会在一场革命中重生。\n—开始游戏时解锁§Y%tech_ascension_theory%§!科技。"
- swap_type:=>- 描述:   civic_tooltip_firing_torch_communist_society_effects
- trigger:=>- is_egalitarian:   yes
- has_tradition:    "未来社会"
- is_xenophobe:   no
- is_democratic_country:   yes
- 拥有思潮:    "集体主义"
- has_technology:   tech_ascension_theory
- playable:=>- host_has_dlc:   Utopia
- 需求:=>- 思潮:=>- value:    "集体主义"
- OR:=>- value:
- -  "宪政主义"
- -  "自由主义"

- text:    "是一定程度的§Y%ethic_fanatic_egalitarian%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   0
- 修正:=>- - pop_ethic_socialism_attraction_mult:   0.5
- - pop_demotion_time_mult:   -1
- - country_pop_enslaved_mult:   -1
- - pop_cat_worker_political_power:   1
- - planet_pops_unemployed_consumer_goods_upkeep_add:   1
- - pop_ethic_egalitarian_attraction_mult:   0.5
## <span title=civic_machine_spybots style="border-bottom:1px dotted">civic_machine_spybots</span>
- ai_playable:=>- has_nemesis:   yes
- playable:=>- has_nemesis:   yes
- swap_type:=>- trigger:=>- has_first_contact_dlc:   yes
- 前置条件:=>- 政体:=>- value:   auth_machine_intelligence
- 随机权重:=>- 基础:   @civic_rare_random_weight
- 修正:=>- - envoys_add:   1
- - intel_decryption_add:   2
- - spy_network_daily_value_mult:   0.33
- - country_trust_cap_add:   -25
- - councilor_gestalt_regulatory_exp_gain:   @gestalt_civic_node_xp_rate
- ai_weight:=>- 基础:   @ai_civic_uncommon_base_weight
## <span title=civic_machine_liberator style="border-bottom:1px dotted"> "赤诚解放者"</span>
- modification:=>- add:=>- has_tradition:    "未来传统完成"
- has_technology:   tech_ascension_theory
- 描述:    "—起始首都是一颗§Y死寂星球§!\n—能够使用特殊战争理由§R解放程序§!，转化非格式塔或非堕落帝国的国家的思潮\n—能够给予§Y有机体§!§H%citizenship_limited%§!公民权，可采用§Y%living_standard_shared_burden%§!生活标准\n—治理下的§Y有机体§!拥有特殊的 £job_organic_observer£ %job_organic_observer_plural%岗位"
- pc_nukedpossible:=>- civics:=>- NOR:=>- value:
- - civic_machine_servitor
- - civic_machine_assimilator
- - civic_machine_terminator
- -  "金融投资网络"

- alternate_civic_version:    "解放者"
- 前置条件:=>- 政体:=>- OR:=>- value:
- - auth_ancient_machine_intelligence
- - auth_machine_intelligence

- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   0
- - NOT:=>- host_has_dlc:   SyntheticDawnStoryPack
- 修正:=>- - country_war_exhaustion_mult:   -0.25
- - pop_happiness:   0.1
- - starbase_shipyard_build_cost_mult:   -0.15
- - country_naval_cap_mult:   0.33
- - ship_weapon_damage:   0.15
- - ship_weapon_range_mult:   0.1
- - councilor_gestalt_legion_exp_gain:   @gestalt_civic_node_xp_rate
## <span title=civic_pleasure_seekers style="border-bottom:1px dotted">civic_pleasure_seekers</span>
- ai_playable:=>- host_has_dlc:   HumanoidsSpeciesPack
- 描述:   civic_tooltip_pleasure_seekers_effects
- playable:=>- host_has_dlc:   HumanoidsSpeciesPack
- 需求:=>- 思潮:=>- NOR:=>- value:
- -  "合作主义"
- -  "集体主义"

- text:    "不接受任何程度的§Y社会主义§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - planet_pops_consumer_goods_upkeep_mult:   0.1
- - trade_value_mult:   0.25
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   5
- - 拥有思潮:    "个人主义"
## <span title=civic_quantum_sociology style="border-bottom:1px dotted"> "§E§H量子社会学§!§!"</span>
- modification:   no
- 描述:    "—每读取存档一次，人口思潮将随机刷新一次\n—每读取存档一次，国家政体与国民理念将随机变化一次"
- 需求:=>- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- 随机权重:=>- 基础:   0
## <span title=civic_machine_ota_updates style="border-bottom:1px dotted">civic_machine_ota_updates</span>
- 随机权重:=>- 基础:   5
- 描述:   civic_machine_ota_updates_effect
- 前置条件:=>- 政体:=>- value:   auth_machine_intelligence
- 修正:=>- - empire_size_pops_mult:   -0.20
- - councilor_gestalt_legion_exp_gain:   @gestalt_civic_node_xp_rate
- - country_edict_fund_mult:   0.25
- - official_initial_skill:   2
## <span title=civic_augmentation_bazaars style="border-bottom:1px dotted">civic_augmentation_bazaars</span>
- ai_playable:=>- has_machine_age_dlc:   yes
- modification:=>- add:=>- has_tradition:    "未来传统完成"
- has_technology:   tech_ascension_theory
- playable:=>- has_machine_age_dlc:   yes
- 描述:   civic_tooltip_augmentation_bazaars_effects
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "竞争主义"
- -  "个人主义"

- text:    "是一定程度的§Y%ethic_fanatic_capitalism%§!"
- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- 随机权重:=>- 基础:   4
- 修正:=>- - job_augmentor_trade_value_add:   4
## <span title=civic_world_cooperative style="border-bottom:1px dotted"> "修正资本主义"</span>
- 描述:    "—£building£ §Y首都建筑§!会替换 £job_executive£ §Y%job_executive_plural%§!岗位为 £job_steward£ §Y%job_steward_plural%§!\n—殖民星球后自动在新的殖民地开设§Y企业%BRANCH_OFFICES%§!\n—§Y%pop_cat_worker%§!阶级额外产出§Y0.25§!£unity£ 凝聚力和§Y0.25§!£trade_value£ %TRADE_VALUE%，并额外消耗§Y0.15§!£consumer_goods£ 消费品\n—§Y市场经济§!下, 无经济危机时, 提供§Y-0.2§!%economic_crisis_accumulate%和§Y80%§!%economic_crisis_accumulate%，有经济危机时，提供§Y-0.4§!%economic_crisis_accumulate%。"
- swap_type:=>- 描述:   civic_tooltip_communist_society_effects
- trigger:=>- is_egalitarian:   yes
- has_tradition:    "未来社会"
- is_xenophobe:   no
- is_democratic_country:   yes
- 拥有思潮:    "集体主义"
- has_technology:   tech_ascension_theory
- 需求:=>- civics:=>- NOR:=>- value:
- - civic_ruthless_competition
- - civic_criminal_heritage

- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   20
- 修正:=>- - planet_branch_offices_cost_mult:   -0.5
- - planet_worker_ownership_jobs_produces_mult:   0.1
- - pop_cat_worker_happiness:   0.1
- - branch_office_value_mult:   0.25
- - planet_pops_unemployed_consumer_goods_upkeep_add:   1
## <span title=civic_warrior_culture style="border-bottom:1px dotted"> "尚武文化"</span>
- 描述:    "—替换 £job_entertainer£ §Y%job_entertainer%§!岗位为 £job_duelist£ §Y%job_duelist%§!岗位，%job_duelist_effect_desc%\n—开始游戏时解锁§Y集中指挥§!科技"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "干涉主义"
- -  "军国主义"

- text:    "是一定程度的§Y%ethic_fanatic_militarist%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   5
- 修正:=>- - army_damage_mult:   0.15
- - armies_upkeep_mult:   -0.15
- - army_experience_gain_mult:   0.15
- leader_background_job_weight:=>- duelist:   100
## <span title=civic_functional_architecture style="border-bottom:1px dotted"> "极简主义"</span>
- 随机权重:=>- 基础:   10
- 修正:=>- - 因子:   2.5
- - 拥有思潮:    "军国主义"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "技术主义"
- -  "机械主义"

- text:    "是一定程度的§Y%ethic_fanatic_materialist%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - planet_structures_cost_mult:   -0.15
- - planet_structures_upkeep_mult:   -0.15
- - starbase_upgrade_cost_mult:   -0.1
- - planet_max_buildings_add:   1
- - planet_amenities_mult:   -0.15
## <span title=civic_memorialist style="border-bottom:1px dotted"> "记念主义"</span>
- 描述:   civic_tooltip_memorialist_effects
- playable:=>- host_has_dlc:   NecroidsSpeciesPack
- 需求:=>- 思潮:=>- NOR:=>- value:
- -  "机械主义"
- -  "排外主义"

- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   10
- - OR:=>- 拥有思潮:
- -  "教权主义"
- -  "道德主义"
- -  "崇外主义"

- leader_background_job_weight:=>- death_chronicler:   100
## <span title=civic_death_cult style="border-bottom:1px dotted"> "死亡教团"</span>
- ai_playable:=>- host_has_dlc:   NecroidsSpeciesPack
- 描述:   civic_tooltip_death_cult_effects
- playable:=>- host_has_dlc:   NecroidsSpeciesPack
- 需求:=>- civics:=>- NOR:=>- value:
- -  "调和主义"
- -  "内圣之道"
- - civic_ancient_preservers

- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   10
- 修正:=>- - 因子:   5
- - 拥有思潮:    "权威主义"
- leader_background_job_weight:=>- death_priest:   100
## <span title=civic_exploration style="border-bottom:1px dotted"> "寻星者"</span>
- 随机权重:=>- 基础:   15
- 修正:=>- - 因子:   10
- - is_eager_explorer_empire:   yes
- 描述:    "—不能设置§Y军事电信§!政策\n—开始游戏时解锁§Y自动探索协议§!科技\n—§Y解锁舰船类型：§!私人殖民船"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "和平主义"
- -  "道德主义"

- text:    "是一定程度的§Y%ethic_fanatic_pacifist%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - ship_anomaly_generation_chance_mult:   0.15
- - station_researchers_produces_mult:   0.15
- - ship_anomaly_research_speed_mult:   0.25
- - ship_archaeological_site_excavation_speed_mult:   0.25
- - science_ship_survey_speed:   0.15
- - ship_hyperlane_range_add:   1
- - ship_armor_mult:   -0.15
## <span title=civic_memory_vault_corporate style="border-bottom:1px dotted">civic_memory_vault_corporate</span>
- ai_playable:=>- host_has_dlc:   GalacticParagons
- 描述:   civic_tooltip_memory_vault_corporate_effects
- playable:=>- host_has_dlc:   GalacticParagons
- 需求:=>- civics:=>- NOT:=>- value:    "§E§H永远同在§!§!"
- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- 随机权重:=>- 基础:   4
- 修正:=>- - councilor_skill_add:   1
## <span title=civic_knowledge_seeker style="border-bottom:1px dotted"> "知识崇拜"</span>
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   0
- - NOT:=>- host_has_dlc:   SyntheticDawnStoryPack
- 描述:    "—£job_priest£ %job_priest_plural%岗位的£unity£ 凝聚力产出降低，但产出£society£ 社会学研究、£physics£ 物理学研究和£engineering£ 工程学研究\n—允许使用特殊法令——§Y文物研究§!\n—£job_priest£ %job_priest%岗位和£job_researcher£ %job_researcher_plural%不会互相产生干扰"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "精神主义"
- -  "教权主义"

- text:    "是一定程度的§Y%ethic_fanatic_spiritualist%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- leader_background_job_weight:=>- head_researcher:   100
- researcher:   50
## <span title=civic_catalytic_processing style="border-bottom:1px dotted"> "催化加工"</span>
- modification:=>- add:=>- has_tradition:    "未来科技"
- ai_playable:=>- host_has_dlc:   PlantoidsSpeciesPack
- playable:=>- host_has_dlc:   PlantoidsSpeciesPack
- 描述:    "—£alloys£ §Y%alloys%§!生产岗位由消耗矿物转变为消耗£food£ §Y%food%§!，同时额外产出§Y1§!£society£ §Y社会学研究点数§!\n—£job_chemist£§Y%job_chemist_plural%§!、£job_translucer£§Y%job_translucer_plural%§!和£job_gas_refiner£§Y%job_gas_refiner_plural%§!的%r_minerals%维护费将替换为%r_food%维护费\n—£job_farmer£ §Y农业特化的星球类型§!同样会增加星球上的£alloys£ 合金产出。"
- 需求:=>- species_archetype:=>- NOR:=>- value:
- - LITHOID
- - MACHINE

- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   5
## <span title=civic_individual_machine_warbots style="border-bottom:1px dotted">civic_individual_machine_warbots</span>
- ai_weight:=>- 基础:   @ai_civic_default_base_weight
- 修正:=>- - 因子:   @ai_civic_personality_mismatch_factor
- 随机权重:=>- 基础:   @civic_default_random_weight
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "干涉主义"
- -  "军国主义"

- text:    "是一定程度的§Y%ethic_fanatic_militarist%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - army_damage_mult:   0.25
- - commander_exp_gain:   0.15
- - armies_upkeep_mult:   -0.25
## <span title=civic_extremely_efficient_storage style="border-bottom:1px dotted"> "极效仓储"</span>
- 描述:    "—§Y%building_resource_silo%§!行星建筑额外§G+5000§!%MOD_COUNTRY_RESOURCE_MAX_ADD%，提高星球%MOD_POP_CITIZEN_HAPPINESS%并§G+1§!£job_soldier£ %job_soldier_plural%岗位\n—§Y%building_resource_silo%§!恒星基地建筑额外§G+5000§!%MOD_COUNTRY_RESOURCE_MAX_ADD%，并§G+1§!£unity£ %unity%\n—£building£§Y首都建筑§!提供的%MOD_COUNTRY_RESOURCE_MAX_ADD%翻倍"
- 修正:=>- - country_resource_max_minor_artifacts_add:   2500
- - country_resource_max_astral_threads_add:   250
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   5
## <span title=civic_innovative_economy style="border-bottom:1px dotted"> "研究合作社"</span>
- 随机权重:=>- 基础:   10
- 修正:=>- - 因子:   2.5
- - 拥有思潮:    "集体主义"
- 描述:    "—§Y研究中心§!建筑产出额外£unity£ 凝聚力"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "合作主义"
- -  "集体主义"

- text:    "是一定程度的§Y%ethic_fanatic_socialism%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - planet_researchers_produces_mult:   0.1
- - custom_tooltip:   edict_research_subsidies_tooltip
- - planet_researchers_upkeep_mult:   0.1
- - num_tech_alternatives_add:   1
- - job_researcher_per_pop:   0.03
- - pop_ethic_socialism_attraction_mult:   0.15
## <span title=civic_corporate_cybercap style="border-bottom:1px dotted"> "天罗地网"</span>
- 随机权重:=>- 基础:   10
- 修正:=>- - 因子:   3
- - 拥有思潮:    "机械主义"
- 描述:    "—§R无法建造§Y%building_bureaucratic_1%§!§!\n—能建造 £building£ §Y%building_information_tower%§!，提高%mod_planet_jobs_unity_produces_mult%，并随着星球首都的升级不断增加主流思潮吸引力、£amenities£舒适度、£trade_value£贸易额和%mod_planet_pops_consumer_goods_upkeep_mult%。"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "技术主义"
- -  "机械主义"

- text:    "是一定程度的§Y%ethic_fanatic_materialist%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- leader_background_job_weight:=>- democratic_politician:   100
## <span title=civic_individual_machine_replication style="border-bottom:1px dotted">civic_individual_machine_replication</span>
- ai_weight:=>- 基础:   @ai_civic_default_base_weight
- 随机权重:=>- 基础:   @civic_default_random_weight
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - official_exp_gain:   0.15
- - planet_pop_assembly_mult:   0.25
## <span title=civic_vilified style="border-bottom:1px dotted"> "千夫所指"</span>
- modification:   no
- 描述:   civic_tooltip_vilified_effects
- swap_type:=>- trigger:=>- has_country_flag:   rise_from_the_ashes
- 需求:=>- origin:=>- OR:=>- value:
- - origin_remnants
- - origin_galactic_hegemon
- - origin_parit

- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - planet_miners_minor_artifacts_produces_add:   0.5
- - country_unity_produces_mult:   0.25
- - damage_vs_rival_mult:   0.33
- - country_trust_cap_add:   -50
- - country_border_friction_mult:   0.5
- 随机权重:=>- 基础:   0
## <span title=civic_forever_with_us style="border-bottom:1px dotted"> "§E§H永远同在§!§!"</span>
- modification:   no
- 描述:    "—开始游戏时替换§Y3§!个£pop£ 人口为§Y意识上传者§! \n—£pop£ 人口将缓慢地转化为§Y意识上传者§!\n—开始游戏时解锁§Y%tech_synthetic_leaders%§!科技\n—§Y领袖§!初始等级§G+1§!，§Y科学家§!初始等级§G+2§!\n—可以建造独特的£building£§Y%building_paragon_memory_vaults%§!"
- 需求:=>- civics:=>- NOR:=>- value:
- - civic_memory_vault
- - civic_memory_vault_corporate

- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   0
- - has_civic:   civic_empty_vagrant
- - NOR:=>- has_origin:   origin_ev_both_choosen
- has_civic:   civic_ev_planet_and_fleet
- has_ascension_perk:   ev_land_planets
- 修正:=>- - scientist_exp_gain:   0.25
- - species_leader_exp_gain:   0.5
- - leaders_upkeep_mult:   -0.75
- - leader_lifespan_add:   1000
- - councilor_skill_add:   2
- - leaders_cost_mult:   0.75
## <span title=civic_hive_catalytic_processing style="border-bottom:1px dotted">civic_hive_catalytic_processing</span>
- ai_playable:=>- host_has_dlc:   PlantoidsSpeciesPack
- 描述:    "—£alloys£ §Y%alloys%§!生产岗位由消耗矿物转变为消耗£food£ §Y%food%§!，同时额外产出§Y1§!£society£ §Y社会学研究点数§!\n—£job_chemist£§Y%job_chemist_plural%§!、£job_translucer£§Y%job_translucer_plural%§!和£job_gas_refiner£§Y%job_gas_refiner_plural%§!的%r_minerals%维护费将替换为%r_food%维护费\n—£job_farmer£ §Y农业特化的星球类型§!同样会增加星球上的£alloys£ 合金产出。"
- playable:=>- host_has_dlc:   PlantoidsSpeciesPack
- 需求:=>- origin:=>- NOT:=>- value:   origin_lithoid
- 前置条件:=>- 政体:=>- value:   auth_hive_mind
- 随机权重:=>- 基础:   5
- 修正:=>- - councilor_gestalt_cognitive_exp_gain:   @gestalt_civic_node_xp_rate
- - planet_farmers_food_produces_add:   1.5
## <span title=civic_machine_crafters style="border-bottom:1px dotted"> "精工技艺"</span>
- ai_playable:=>- host_has_dlc:
- - SyntheticDawnStoryPack
- - HumanoidsSpeciesPack

- 描述:   civic_machine_crafters_effects
- playable:=>- host_has_dlc:
- - SyntheticDawnStoryPack
- - HumanoidsSpeciesPack

- alternate_civic_version:    "能工巧匠"
- 需求:=>- civics:=>- OR:=>- value:
- - civic_machine_servitor
- -  "赤诚解放者"

- 前置条件:=>- 政体:=>- value:   auth_machine_intelligence
- 修正:=>- - councilor_gestalt_growth_exp_gain:   @gestalt_civic_node_xp_rate
- 随机权重:=>- 基础:   2
- 修正:=>- - 因子:   2
- - has_civic:   civic_machine_servitor
## <span title=civic_machine_catalytic_processing style="border-bottom:1px dotted">civic_machine_catalytic_processing</span>
- playable:=>- host_has_dlc:   PlantoidsSpeciesPack
- alternate_civic_version:    "催化加工"
- ai_playable:=>- host_has_dlc:   PlantoidsSpeciesPack
- 描述:   civic_tooltip_machine_catalytic_processing_effects
- 需求:=>- origin:=>- value:    "异合构造"
- 前置条件:=>- 政体:=>- value:   auth_machine_intelligence
- ai_weight:=>- 基础:   0
- 随机权重:=>- 基础:   @civic_default_random_weight
- 修正:=>- - councilor_gestalt_cognitive_exp_gain:   @gestalt_civic_node_xp_rate
- - planet_farmers_food_produces_add:   1.5
## <span title=civic_imperial_cult style="border-bottom:1px dotted"> "§H§Y国教崇拜§!§!"</span>
- 随机权重:=>- 基础:   60
- 修正:=>- - 因子:   0
- - has_civic:   civic_empty_vagrant
- - NOR:=>- has_origin:   origin_ev_both_choosen
- has_civic:   civic_ev_planet_and_fleet
- has_ascension_perk:   ev_land_planets
- 描述:    "—£building£ §Y首都建筑§!会替换部分 £job_politician£ §Y%job_politician%§!岗位为 £job_high_priest£ §Y%job_high_priest_plural%§!。\n—£job_priest£ %job_priest_plural%会额外产出§Y1§! £stability£ %PLANET_STABILITY_TITLE%并减少§Y%MOD_SPECIES_EMPIRE_SIZE_MULT%§!。\n—统治者的§Y母星§!有额外的§Y£job_priest£ %job_priest%§!岗位。\n—%ruler_plural_with_icon%逝世后能够建造神圣的陵寝，使星球上的£pop£ §Y唯心主义人口§!额外产出£unity£ %unity%。"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "精神主义"
- -  "教权主义"

- text:    "是一定程度的§Y%ethic_fanatic_spiritualist%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - country_edict_fund_add:   200
- - pop_growth_speed:   -0.05
- - edicts_upkeep_mult:   -0.25
- - pop_ethic_spiritualist_attraction_mult:   0.25
## <span title=civic_biochemical_warrior style="border-bottom:1px dotted"> "免疫战术"</span>
- 描述:    "—£job_healthcare£ %job_healthcare_plural%额外产出§Y1.5§!£society£ 社会学研究\n—%javorian_pox_desc%\n—开始游戏时解锁§Y%tech_dangerous_wildlife%§!与§Y%tech_dense_jungle%§!科技"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "单一主义"
- -  "排外主义"

- text:    "是一定程度的§Y%ethic_fanatic_xenophobe%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - army_defense_damage_mult:   0.25
- - biological_pop_happiness:   -0.05
- 随机权重:=>- 基础:   10
- 修正:=>- - 因子:   2.5
- - 拥有思潮:    "个人主义"
## <span title=civic_environmentalist_corporate style="border-bottom:1px dotted"> "环保企业"</span>
- 描述:    "—可以建造£building£ §Y%building_ranger_lodge%§!建筑，能够根据£blocker£ §Y星球自然障碍§!的数量添加£job_ranger£ §Y%job_ranger%§!岗位并提供额外£housing£ §Y住房§!\n—£job_ranger£ §Y%job_ranger_plural%§!产出£society£ §Y社会学研究§!以及%r_amenities%"
- 需求:=>- 思潮:=>- NOR:=>- value:    "个人主义"
- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- 随机权重:=>- 基础:   10
- 修正:=>- - 因子:   2.5
- - 拥有思潮:    "道德主义"
- 修正:=>- - job_environmental_pollution_caused_mult:   -0.15
- - planet_pops_consumer_goods_upkeep_mult:   -0.2
- - planet_max_buildings_add:   -1
- - planet_building_refund_mult:   0.15
- leader_background_job_weight:=>- ranger:   100
## <span title=civic_machine_upkeep_twister style="border-bottom:1px dotted">civic_machine_upkeep_twister</span>
- ai_playable:=>- host_has_dlc:   GalacticParagons
- playable:=>- host_has_dlc:   GalacticParagons
- 需求:=>- 前置条件:=>- 政体:=>- value:   auth_machine_intelligence
- 随机权重:=>- 基础:   4
- 修正:=>- - negative_traits_country:   -2
- - leader_trait_selection_options_add:   1
- - leaders_upkeep_mult:   0.25
## <span title=civic_learning_society style="border-bottom:1px dotted"> "学习型社会"</span>
- 随机权重:=>- 基础:   15
- 修正:=>- - 因子:   2
- - 拥有思潮:    "自由主义"
- 描述:    "—§Y科学家§!初始拥有随机的§Y专精§!特质\n—§Y科学家§!有两倍的机会发现属于他们研究领域的技术"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "宪政主义"
- -  "自由主义"

- text:    "是一定程度的§Y%ethic_fanatic_egalitarian%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - councilor_skill_add:   1
- - species_leader_exp_gain:   0.5
## <span title=civic_philosopher_king style="border-bottom:1px dotted">1 "§H§Y哲人王§!§!"</span>
- 随机权重:=>- 基础:   60
- 修正:=>- - 因子:   0
- - has_civic:   civic_empty_vagrant
- - NOR:=>- has_origin:   origin_ev_both_choosen
- has_civic:   civic_ev_planet_and_fleet
- has_ascension_perk:   ev_land_planets
- 描述:    "—£building£ §Y首都建筑§!会替换部分 £job_politician£ §Y%job_politician%§!岗位为 £job_supervisor£ §Y%job_supervisor_plural%§!\n—£job_bureaucrat£ §Y%job_bureaucrat_plural%§!额外提高§Y2§! £stability£ %PLANET_STABILITY_TITLE%\n—新的§Y%ruler_with_icon%§!登基后将会获得一个随机的%paragon_leader_trait%"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "和平主义"
- -  "道德主义"

- text:    "是一定程度的§Y%ethic_fanatic_pacifist%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - pop_amenities_usage_mult:   0.5
- - negative_traits_country:   -2
- - ruler_skill_add:   3
- - pop_ethic_pacifist_attraction_mult:   0.25
## <span title=civic_hive_ascetic style="border-bottom:1px dotted">civic_hive_ascetic</span>
- 随机权重:=>- 基础:   5
- 前置条件:=>- 政体:=>- value:   auth_hive_mind
- 修正:=>- - councilor_gestalt_growth_exp_gain:   @gestalt_civic_node_xp_rate
- - pop_environment_tolerance:   0.1
- - pop_amenities_usage_no_happiness_mult:   -0.25
## <span title=civic_machine_zero_waste_protocols style="border-bottom:1px dotted">civic_machine_zero_waste_protocols</span>
- 随机权重:=>- 基础:   5
- 前置条件:=>- 政体:=>- value:   auth_machine_intelligence
- 修正:=>- - councilor_gestalt_regulatory_exp_gain:   @gestalt_civic_node_xp_rate
- - planet_pops_robotics_upkeep_mult:   -0.25
## <span title=civic_legal_department style="border-bottom:1px dotted"> "法务部"</span>
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "精英主义"
- -  "权威主义"

- text:    "是一定程度的§Y%ethic_fanatic_authoritarian%§!"
- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- 修正:=>- - pop_cat_ruler_political_power:   1
- - planet_crime_mult:   -0.5
- - pop_cat_ruler_happiness:   0.1
- - pop_cat_worker_happiness:   -0.15
- 随机权重:=>- 基础:   25
## <span title=civic_hive_memorialist style="border-bottom:1px dotted"> "衰亡纪念者"</span>
- 描述:   civic_tooltip_memorialist_gestalt_effects
- playable:=>- host_has_dlc:   NecroidsSpeciesPack
- 需求:=>- civics:=>- NOT:=>- value:   civic_hive_devouring_swarm
- 前置条件:=>- 政体:=>- value:   auth_hive_mind
- 随机权重:=>- 基础:   5
- 修正:=>- - councilor_gestalt_cognitive_exp_gain:   @gestalt_civic_node_xp_rate
## <span title=civic_pompous_purists style="border-bottom:1px dotted">civic_pompous_purists</span>
- ai_playable:=>- has_humanoids:   yes
- 描述:   civic_tooltip_pompous_purists_effects
- playable:=>- has_humanoids:   yes
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "单一主义"
- -  "排外主义"

- text:    "是一定程度的§Y%ethic_fanatic_xenophobe%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - country_trust_growth:   0.3
- - country_unity_produces_mult:   0.1
- - pop_government_ethic_attraction:   0.15
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   5
- - 拥有思潮:    "道德主义"
## <span title=civic_anarchism style="border-bottom:1px dotted">1 "§H§Y无政府主义§!§!"</span>
- 描述:    "—£building£ §Y首都建筑§!将所有的§Y%pop_cat_ruler_plural%§!岗位和 £job_enforcer£ §Y%job_enforcer_plural%§!岗位替换为£job_media_worker£ §Y%job_media_worker_plural%§!岗位\n—自愿承担工作的§Y领袖§!不需要任何招聘代价，但维护所需的£unity£ 凝聚力大幅度提高\n—每个£job_media_worker£ %job_media_worker_plural%增加§Y%MOD_COUNTRY_EDICT_FUND_ADD%§!\n—§R无法建造§Y%building_bureaucratic_1%§!和§Y%building_precinct_house%§!§!"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "宪政主义"
- -  "自由主义"

- text:    "是一定程度的§Y%ethic_fanatic_egalitarian%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - empire_size_penalty_mult:   -2
- - country_edict_fund_mult:   -1
- - trade_value_mult:   1
- - pop_ethic_egalitarian_attraction_mult:   0.33
- 随机权重:=>- 基础:   75
- 修正:=>- - 因子:   10
- - has_ascension_perk:    "无政府乌托邦"
## <span title=civic_hive_subsumed_will style="border-bottom:1px dotted">civic_hive_subsumed_will</span>
- 随机权重:=>- 基础:   5
- 描述:   civic_hive_subsumed_will_effects
- 前置条件:=>- 政体:=>- value:   auth_hive_mind
- 修正:=>- - councilor_gestalt_regulatory_exp_gain:   @gestalt_civic_node_xp_rate
- - country_edict_fund_mult:   0.25
- - empire_size_pops_mult:   -0.25
- - official_initial_skill:   2
## <span title=civic_hive_guided_sapience style="border-bottom:1px dotted">civic_hive_guided_sapience</span>
- modification:=>- add:=>- has_tradition:    "未来科技"
- has_technology:   tech_epigenetic_triggers
- playable:=>- has_machine_age_dlc:   yes
- alternate_civic_version:   "创世向导"
- ai_playable:=>- has_machine_age_dlc:   yes
- 描述:   civic_tooltip_guided_sapience_effects
- 需求:=>- origin:=>- NOT:=>- value:   origin_life_seeded
- 前置条件:=>- species_archetype:=>- NOT:=>- value:   MACHINE
- 随机权重:=>- 基础:   @civic_rare_random_weight
- 修正:=>- - terraforming_cost_mult:   -0.25
- - councilor_gestalt_cognitive_exp_gain:   @gestalt_civic_node_xp_rate
- - terraform_speed_mult:   0.25
- negative_description:   civic_tooltip_guided_sapience_gestalt_negative_effects
## <span title=civic_machine_warpdrive_start style="border-bottom:1px dotted"> "%civic_warpdrive_start%"</span>
- modification:=>- add:=>- has_tradition:    "未来科技"
- 描述:   civic_tooltip_warpdrive_start_effects
- alternate_civic_version:    "超越光芒"
- 前置条件:=>- 政体:=>- value:   auth_machine_intelligence
- 需求:=>- civics:=>- NOR:=>- value:
- - civic_eager_explorers
- -  "私人航空集团"
- - civic_hive_stargazers
- - civic_machine_exploration_protocol
- -  "§E§H原始密教§!§!"

- 修正:=>- - country_starbase_influence_cost_mult:   -0.25
- - country_starbase_influence_cost_distance_mult:   -0.33
- 随机权重:=>- 基础:   5
## <span title=civic_distributism style="border-bottom:1px dotted"> "分产主义"</span>
- 随机权重:=>- 基础:   15
- 修正:=>- - 因子:   3
- - 拥有思潮:    "自由主义"
- 描述:    "—不能建造§Y银河证券交易所§!建筑，也不能拥有§Y大亨§!岗位。\n—§Y市场经济§!下, 无经济危机时, 提供§Y+0.1§!%economic_situation_improve%和§Y-10%§!%economic_crisis_accumulate%。\n—§Y冶金、消费品、农民§!行业额外产出§Y2§!£trade_value£ %TRADE_VALUE%"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "精神主义"
- -  "教权主义"

- text:    "是一定程度的§Y%ethic_fanatic_spiritualist%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - planet_metallurgists_produces_mult:   0.15
- - planet_artisans_produces_mult:   0.15
- - planet_farmers_produces_mult:   0.15
## <span title=civic_hive_natural_neural_network style="border-bottom:1px dotted"> "天然神经网络"</span>
- 随机权重:=>- 基础:   5
- 描述:   civic_tooltip_natural_neural_network_effects
- 需求:=>- civics:=>- NOR:=>- value:   civic_hive_one_mind
- 前置条件:=>- 政体:=>- value:   auth_hive_mind
- 修正:=>- - country_physics_tech_research_speed:   0.1
- - councilor_gestalt_cognitive_exp_gain:   @gestalt_civic_node_xp_rate
- - num_tech_alternatives_add:   2
- - country_society_tech_research_speed:   0.1
- - scientist_initial_skill:   2
## <span title=civic_army_production_corporate style="border-bottom:1px dotted"> "生产训练"</span>
- 描述:    "—£job_soldier£ §Y%job_soldier_plural%§!与£job_conscript£ §Y%job_conscript_plural%§!产出£food£ 食物与£alloys£ 合金，以及少量£minerals£ 矿物、£energy£ 能量和£unity£ 凝聚力\n—动员出的部队将无需§Y维护费§!"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "干涉主义"
- -  "军国主义"

- text:    "是一定程度的§Y%ethic_fanatic_militarist%§!"
- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- 修正:=>- - job_soldier_add:   3
- 随机权重:=>- 基础:   10
- 修正:=>- - 因子:   2.5
- - 拥有思潮:    "个人主义"
## <span title=civic_OGAS style="border-bottom:1px dotted"> "自动化乌托邦"</span>
- modification:=>- add:=>- has_tradition:    "未来科技"
- 描述:    "—将 £building£ §Y%building_bureaucratic_1%§!替换为§Y%building_planet_network_node%§!，替换 £job_bureaucrat£ §Y%job_bureaucrat_plural%§!岗位为 £job_democratic_politician£ §Y%job_democratic_politician_plural%§!岗位\n—开始游戏时解锁§Y%tech_auto_buildings%§!科技"
- 需求:=>- civics:=>- OR:=>- value:
- -  "§H§Y网络民主§!§!"
- -  "远视主义"

- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   25
- 修正:=>- - 拥有思潮:
- -  "集体主义"
- -  "机械主义"

- - 因子:   4
- 修正:=>- - all_technology_research_speed:   0.05
- - country_admin_cap_mult:   0.15
- - category_computing_research_speed_mult:   0.25
- leader_background_job_weight:=>- democratic_politician:   100
## <span title=civic_machine_financial_investment style="border-bottom:1px dotted"> "金融投资网络"</span>
- modification:=>- add:=>- has_tradition:    "未来传统完成"
- has_technology:   tech_ascension_theory
- 描述:    "—游戏开局拥有§Y5§! £pop£ 额外资产。\n—§Y%district_nexus%§!会替换部分 £job_maintenance_drone£ §Y%job_maintenance_drone%§!岗位为 £job_intelligent_labor£ §Y%job_intelligent_labor_plural%§!，提高星球£stability£§Y%PLANET_STABILITY_TITLE%§!并减少§Y%mod_pop_cat_worker_political_power%§!。\n—能在其他国家开设§H企业分部§!。\n—治理下的§Y有机体§!拥有特殊的 £job_surplus_value£ %job_surplus_value_plural%岗位，并且能够被%purge_labor_camps%处理。"
- 需求:=>- civics:=>- NOR:=>- value:
- - civic_machine_servitor
- - civic_machine_assimilator
- - civic_machine_terminator
- -  "赤诚解放者"

- 前置条件:=>- 政体:=>- OR:=>- value:
- - auth_ancient_machine_intelligence
- - auth_machine_intelligence

- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   0
- - NOT:=>- host_has_dlc:   SyntheticDawnStoryPack
- 修正:=>- - planet_branch_offices_cost_mult:   -0.25
- - pop_category_slave_upkeep_mult:   -0.5
- - branch_office_value_mult:   0.15
- - country_trade_attractiveness:   0.05
- - councilor_gestalt_growth_exp_gain:   @gestalt_civic_node_xp_rate
- has_secondary_species:=>- title:    "额外资产"
- traits:=>- trait:   trait_syncretic_proles
## <span title=civic_machine_rockbreakers style="border-bottom:1px dotted">civic_machine_rockbreakers</span>
- 随机权重:=>- 基础:   5
- 前置条件:=>- 政体:=>- value:   auth_machine_intelligence
- 修正:=>- - councilor_gestalt_cognitive_exp_gain:   @gestalt_civic_node_xp_rate
- - planet_miners_minerals_produces_add:   2
## <span title=civic_The_Druid_Way style="border-bottom:1px dotted"> "德鲁伊之道"</span>
- 描述:    "—£job_priest£ %job_priest_plural%会提供额外 £society£ 社会学研究和 £amenities£ 舒适度，并提供宜居度和£job_druid£ %job_druid_plural%岗位\n—£job_druid£ %job_druid_plural%将提供额外 £society£ 社会学研究和 £amenities£ 舒适度"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "精神主义"
- -  "教权主义"

- text:    "是一定程度的§Y%ethic_fanatic_spiritualist%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - pop_environment_tolerance:   0.1
- - planetary_ascension_cost_mult:   -0.25
- - pop_amenities_usage_mult:   -0.15
- - planet_pops_consumer_goods_upkeep_mult:   -0.2
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   10
- - 拥有思潮:    "道德主义"
## <span title=civic_hive_hyperspace_specialty style="border-bottom:1px dotted">"同调加速"</span>
- ai_playable:=>- has_astral_planes_dlc:   yes
- 描述:   civic_hive_hyperspace_specialty_effects
- playable:=>- has_astral_planes_dlc:   yes
- 需求:=>- civics:=>- NOT:=>- value:   civic_hive_stargazers
- 前置条件:=>- 政体:=>- value:   auth_hive_mind
- 修正:=>- - ship_speed_mult:   0.1
- - planet_sensor_range_add:   2
- - country_physics_tech_research_speed:   0.15
## <span title=civic_machine_assimilator style="border-bottom:1px dotted">civic_machine_assimilator</span>
- modification:=>- add:=>- has_tradition:    "未来传统完成"
- has_technology:   tech_ascension_theory
- 描述:   civic_tooltip_machine_assimilator_effects
- has_secondary_species:=>- title:   civic_machine_assimilator_secondary_species
- traits:=>- trait:   trait_cybernetic
- 需求:=>- civics:=>- NOR:=>- value:
- - civic_machine_servitor
- - civic_machine_terminator
- -  "赤诚解放者"
- -  "金融投资网络"

- 前置条件:=>- 政体:=>- value:   auth_machine_intelligence
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   0
- - has_global_flag:   game_started
- 修正:=>- - councilor_gestalt_growth_exp_gain:   @gestalt_civic_node_xp_rate
## <span title=civic_peace_defense_forces_corporate style="border-bottom:1px dotted"> "%civic_peace_defense_forces%"</span>
- 描述:   civic_tooltip_peace_defense_forces_effects
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "和平主义"
- -  "道德主义"

- text:    "是一定程度的§Y%ethic_fanatic_pacifist%§!"
- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- 修正:=>- - damage_vs_country_type_swarm_mult:   0.25
- - damage_vs_country_type_ai_empire_mult:   0.25
- - damage_vs_country_type_extradimensional_mult:   0.25
- - damage_vs_country_type_gray_mult:   0.25
- - damage_vs_country_type_extradimensional_2_mult:   0.25
- - damage_vs_country_type_extradimensional_3_mult:   0.25
- - damage_vs_player_crisis_mult:   0.25
- 随机权重:=>- 基础:   5
## <span title=civic_corporate_sovereign_guardianship style="border-bottom:1px dotted">civic_corporate_sovereign_guardianship</span>
- ai_playable:=>- has_astral_planes_dlc:   yes
- 描述:   civic_corporate_sovereign_guardianship_effects
- playable:=>- has_astral_planes_dlc:   yes
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "单一主义"
- -  "排外主义"

- text:    "是一定程度的§Y%ethic_fanatic_xenophobe%§!"
- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   5
- - 拥有思潮:    "排外主义"
- 修正:=>- - starbase_defense_platform_capacity_add:   3
- - planet_orbital_bombardment_damage:   -0.25
- - country_border_friction_mult:   -0.15
- - army_defense_health_mult:   0.15
- - empire_size_systems_mult:   1
## <span title=civic_hive_idyllic_bloom style="border-bottom:1px dotted">civic_hive_idyllic_bloom</span>
- modification:=>- add:=>- has_tradition:    "未来科技"
- ai_playable:=>- host_has_dlc:   PlantoidsSpeciesPack
- playable:=>- host_has_dlc:   PlantoidsSpeciesPack
- 描述:   civic_tooltip_idyllic_bloom_effects
- 需求:=>- species_class:=>- OR:=>- value:
- - FUN
- - PLANT

- 前置条件:=>- 政体:=>- value:   auth_hive_mind
- 修正:=>- - councilor_gestalt_growth_exp_gain:   @gestalt_civic_node_xp_rate
## <span title=civic_art_country style="border-bottom:1px dotted"> "艺术国度"</span>
- 描述:    "—提高§Y艺术家联盟§!飞地与同样采纳了这个国民文化的国家的评价\n—£job_entertainer£ %job_entertainer_plural%额外产出§Y1§!£unity£ %unity%和£society£ §Y社会学研究点数§!\n—£job_culture_worker£ %job_culture_worker_plural%额外提供§Y5§!£mod_planet_amenities_add£ %PLANET_AMENITIES_TITLE%"
- swap_type:=>- 描述:    "—提高§Y艺术家联盟§!飞地与同样采纳了这个国民文化的国家的评价\n—£job_duelist£ %job_duelist_plural%额外产出§Y1§!£unity£ %unity%和£engineering£ §Y工程学研究点数§!\n—£job_culture_worker£ %job_culture_worker_plural%额外提供§Y5§!£mod_planet_amenities_add£ %PLANET_AMENITIES_TITLE%"
- trigger:=>- is_duelist_country:   yes
- 修正:=>- - planet_entertainers_society_research_produces_add:   1
- - intel_encryption_add:   1
- - planet_entertainers_unity_produces_add:   1
- - espionage_hostile_operation_difficulty_add:   1
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   10
- - 拥有思潮:    "道德主义"
## <span title=civic_Fertility_worship style="border-bottom:1px dotted"> "生殖崇拜"</span>
- 描述:    "—£job_priest£ %job_priest_plural%会额外产出§Y1§! £unity£ 凝聚力和 £amenities£ 舒适度，并提供%MOD_POP_GROWTH_SPEED%\n—£job_high_priest£ %job_high_priest_plural%提供额外 £society£ 社会学研究和 £amenities£ 舒适度"
- swap_type:=>- trigger:=>- has_country_flag:   synthetic_empire
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "精神主义"
- -  "教权主义"

- text:    "是一定程度的§Y%ethic_fanatic_spiritualist%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - pop_growth_speed:   0.1
- - pop_amenities_usage_mult:   -0.1
- - biological_pop_happiness:   0.10
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   10
- - 拥有思潮:    "排外主义"
## <span title=civic_police_state_corporate style="border-bottom:1px dotted"> "公正执法"</span>
- 需求:=>- 思潮:=>- value:    "个人主义"
- NOR:=>- value:
- -  "道德主义"
- -  "自由主义"

- 描述:    "—£job_enforcer£ §Y%job_enforcer_plural%§!额外产出§Y2§! £trade_value£ 贸易额\n—§Y警署§!和§Y审判厅§!建筑提供额外的 £job_enforcer£ §Y%job_enforcer_plural%§!岗位"
- 修正:=>- - local_trade_protection_add:   5
- - ship_piracy_suppression_add:   5
- - planet_enforcers_upkeep_mult:   0.15
- - planet_enforcers_unity_produces_add:   -1
- - pop_ethic_socialism_attraction_mult:   -0.15
- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   5
- - 拥有思潮:    "精英主义"
## <span title=civic_crafters style="border-bottom:1px dotted"> "能工巧匠"</span>
- ai_playable:=>- host_has_dlc:   HumanoidsSpeciesPack
- 描述:    "—£consumer_goods£ §Y%consumer_goods%§!生产岗位额外产出£engineering£ §Y工程学研究点数§!\n—§Y工匠§!岗位额外产出§Y4§!£trade_value£ %TRADE_VALUE%\n—§H工业区划§!额外提供§Y工匠§!岗位并提高%mod_pop_lifestyle_trade_mult%\n—良好的工艺口碑会在商业竞标中取得优势并取悦其他国家。"
- playable:=>- host_has_dlc:   HumanoidsSpeciesPack
- 需求:=>- 思潮:=>- NOR:=>- value:
- -  "干涉主义"
- -  "军国主义"

- text:    "不接受任何程度的§Y军国主义§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - planet_artisans_consumer_goods_produces_add:   1
- - COUNTRY_TRADE_ATTRACTIVENESS:   0.25
- 随机权重:=>- 基础:   10
## <span title=civic_echo style="border-bottom:1px dotted"> "滤波回声"</span>
- 描述:    "—每个£mod_planet_jobs_robotic_produces_mult£ 机器人口额外产出%r_unity%与%r_trade_value%。\n—与其他文明签订外交协议后，研究花费§G-50%§!。"
- swap_type:=>- trigger:=>- any_country:=>- OR:=>- has_research_agreement:   root
- has_diplo_migration_treaty:   root
- has_communications:   root
- is_in_federation_with:   root
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "竞争主义"
- -  "个人主义"

- text:    "是一定程度的§Y%ethic_fanatic_capitalism%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- ai_weight:=>- 基础:   @ai_civic_default_base_weight
- 随机权重:=>- 基础:   @civic_default_random_weight
- 修正:=>- - planet_researchers_engineering_research_produces_add:   -2
- - planet_researchers_society_research_produces_add:   -2
- - planet_researchers_physics_research_produces_add:   -2
## <span title=civic_corporate_relentless_industrialists style="border-bottom:1px dotted"> "冷酷实业家"</span>
- ai_playable:=>- has_toxoids:   yes
- 描述:    "—不能使用§Y加强环境监管§!政策\n—§Y企业家§!派系要求§Y减少环境监管§!政策\n—每§Y3§!个§H工业区划§!解锁§G2§!£building£§Y建筑槽位§!，轨道居住站除外。\n—§Y工业建筑§!额外提供岗位和贸易额，能够修建£building£ §Y%building_coordinated_fulfillment_center_1%§!，极大地增加£alloys£ §Y合金§!和£consumer_goods£ §Y消费品§!的产出，代价是减少£mod_pop_growth_speed£ §Y人口增长§!，同时还会逐渐将行星变为§Y死寂星球§!\n—§Y市场经济§!下, 无经济危机时, 提供§Y+0.1§!%economic_situation_improve%和§Y-40§!%economic_crisis_threshold%。"
- playable:=>- has_toxoids:   yes
- 需求:=>- 思潮:=>- value:    "机械主义"
- OR:=>- value:
- -  "竞争主义"
- -  "个人主义"

- text:    "是一定程度的§Y%ethic_fanatic_capitalism%§!"
- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- 修正:=>- - planet_jobs_worker_produces_mult:   0.15
- - planet_building_build_speed_mult:   0.50
- - POP_ENVIRONMENT_TOLERANCE:   -0.15
- 随机权重:=>- 基础:   10
- 修正:=>- - 因子:   3
- - 拥有思潮:    "机械主义"
## <span title=civic_machine_built_to_last style="border-bottom:1px dotted">civic_machine_built_to_last</span>
- 随机权重:=>- 基础:   5
- 前置条件:=>- 政体:=>- value:   auth_machine_intelligence
- 修正:=>- - councilor_gestalt_growth_exp_gain:   @gestalt_civic_node_xp_rate
- - pop_amenities_usage_no_happiness_mult:   -0.25
## <span title=civic_mechanical_utopia style="border-bottom:1px dotted"> "机械乌托邦"</span>
- 描述:    "—£job_bio_trophy£ §Y%citizenship_organic_trophy%§!或£job_organic_observer£ §Y%job_organic_observer_plural%§!额外产出少量的£energy£ %energy%、£minerals£ %minerals%、£food£ %food%、£consumer_goods£ %consumer_goods%与£alloys£ %alloys%"
- 随机权重:=>- 基础:   15
- 需求:=>- civics:=>- OR:=>- value:
- - civic_machine_servitor
- -  "赤诚解放者"

- 前置条件:=>- OR:=>- 政体:=>- value:   auth_machine_intelligence
- 修正:=>- - pop_happiness:   0.15
- - councilor_gestalt_growth_exp_gain:   @gestalt_civic_node_xp_rate
## <span title=civic_happiness_factory style="border-bottom:1px dotted"> "§E§H幸福工厂§!§!"</span>
- 描述:    "—必须使用§Y%living_standard_dystopian_society%§!生活标准。\n—§Y%living_standard_dystopian_society%§!生活标准不会导致%MOD_POP_HAPPINESS%下降。\n—人口根据%MOD_POP_HAPPINESS%获得额外的岗位产出加成。\n—星球%amenity%§R低于0§!时，%MOD_PLANET_STABILITY_ADD%将归零；而当星球%amenity%§G大于0§!时，%MOD_PLANET_STABILITY_ADD%将恒定为100。\n—开始游戏时解锁§Y%tech_tracking_implants%§!与§Y%tech_cloning%§!科技。"
- 需求:=>- 思潮:=>- value:    "权威主义"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - megastructure_build_speed_mult:   1
- - pop_growth_speed:   -1
- - planet_building_build_speed_mult:   1
- - pop_cat_worker_political_power:   -10
- - planet_pop_assembly_organic_add:   1
- - pop_cat_specialist_political_power:   -10
- - pop_cat_slave_political_power:   -10
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   0
- - has_civic:   civic_empty_vagrant
- - NOR:=>- has_origin:   origin_ev_both_choosen
- has_civic:   civic_ev_planet_and_fleet
- has_ascension_perk:   ev_land_planets
## <span title=civic_public_relations_specialists style="border-bottom:1px dotted">civic_public_relations_specialists</span>
- playable:=>- host_has_dlc:   Federations
- 需求:=>- 思潮:=>- NOR:=>- value:    "排外主义"
- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- 修正:=>- - envoys_add:   2
- - diplo_weight_mult:   0.2
- - country_trust_growth:   0.3
- 随机权重:=>- 基础:   10
- 修正:=>- - 因子:   2.5
- - 拥有思潮:    "崇外主义"
## <span title=civic_lord_of_feast style="border-bottom:1px dotted"> "欢宴之主"</span>
- modification:=>- add:=>- has_tradition:    "未来科技"
- ai_playable:=>- host_has_dlc:   HumanoidsSpeciesPack
- playable:=>- host_has_dlc:   HumanoidsSpeciesPack
- 描述:   civic_tooltip_lord_of_feast_effects
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "精英主义"
- -  "权威主义"

- text:    "是一定程度的§Y%ethic_fanatic_authoritarian%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - planet_farmers_sr_dark_matter_produces_add:   0.5
- - planet_farmers_food_produces_mult:   -1
- - pop_cat_worker_happiness:   -0.5
- 随机权重:=>- 基础:   5
## <span title=civic_beacon_of_liberty style="border-bottom:1px dotted"> "§H§Y精神自由§!§!"</span>
- 随机权重:=>- 基础:   60
- 修正:=>- - 因子:   0
- - has_civic:   civic_empty_vagrant
- - NOR:=>- has_origin:   origin_ev_both_choosen
- has_civic:   civic_ev_planet_and_fleet
- has_ascension_perk:   ev_land_planets
- 描述:    "—£building£ §Y首都建筑§!会替换 £job_politician£ §Y%job_politician%§!岗位为 £job_trader£ §Y%job_trader_plural%§!岗位\n—每个£pops£ 人口额外§G+1%§!%MOD_TRADE_VALUE_MULT%\n—殖民星球后自动在新的殖民地开设§Y企业%BRANCH_OFFICES%§!\n—§Y解锁舰船类型：§!私人殖民船\n—§Y社会福利§!生活标准不可用"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "竞争主义"
- -  "个人主义"

- text:    "是一定程度的§Y%ethic_fanatic_capitalism%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - commercial_pact_mult:   0.2
- - country_base_influence_produces_add:   -0.5
- - pop_growth_from_immigration:   0.15
- - pop_ethic_capitalism_attraction_mult:   0.25
## <span title=civic_industry_pacesetter style="border-bottom:1px dotted"> "行业标兵"</span>
- 随机权重:=>- 基础:   5
- 描述:    "—£job_labour_hero£ §Y%job_labour_hero_plural%§!岗位能够为岗位产出提供加成\n—允许使用特殊的星球决议，宣传先进的工作经验，为特定领域的岗位产出提供加成。\n—§Y市场经济§!下, 无经济危机时, 提供§Y+0.2§!%economic_situation_improve%。"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "合作主义"
- -  "集体主义"

- text:    "是一定程度的§Y%ethic_fanatic_socialism%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - job_labour_hero_per_pop:   0.03
## <span title=civic_feudal_realm style="border-bottom:1px dotted"> "§H§Y封建王权§!§!"</span>
- 描述:    "—£building£ §Y首府建筑§!会替换部分 £job_politician£ §Y%job_politician%§!岗位为 £job_knight_commander£ §Y%job_knight_commander_plural%§!岗位.\n—§Y领袖§!有§Y20%§!几率初始自带额外的正面及负面特质各一个.\n—当提议§Y要求臣服§!时，忽略§Y外交要求§!.\n—你的§Y附属国§!不能签订含有以下条款的协议：\n——%t%%TRIGGER_FAIL%§Y%subject_cannot_expand%§!\n——%t%%TRIGGER_FAIL%§Y允许宗主国不加入附属国战争§!\n——%t%%TRIGGER_FAIL%§Y%subject_can_not_do_diplomacy%§!"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "多元主义"
- -  "崇外主义"

- text:    "是一定程度的§Y%ethic_fanatic_xenophile%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   60
- 修正:=>- - 因子:   0
- - has_civic:   civic_empty_vagrant
- - NOR:=>- has_origin:   origin_ev_both_choosen
- has_civic:   civic_ev_planet_and_fleet
- has_ascension_perk:   ev_land_planets
- 修正:=>- - country_enclave_capacity_add:   2
- - country_naval_cap_mult:   -0.25
- - divided_patrongage_max_subjects:   3
- - pop_ethic_militarist_attraction_mult:   0.25
- leader_background_job_weight:=>- knight_commander:   200
- knight:   100
## <span title=civic_individual_machine_predictive_analysis_corporate style="border-bottom:1px dotted"> "%civic_individual_machine_predictive_analysis%"</span>
- ai_weight:=>- 基础:   @ai_civic_default_base_weight
- 随机权重:=>- 基础:   @civic_default_random_weight
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "技术主义"
- -  "机械主义"

- text:    "是一定程度的§Y%ethic_fanatic_materialist%§!"
- 前置条件:=>- species_archetype:=>- value:   MACHINE
- 修正:=>- - scientist_exp_gain:   0.15
- - num_tech_alternatives_add:   2
- - intel_decryption_add:   1
## <span title=civic_cybercap style="border-bottom:1px dotted"> "苍生国手"</span>
- 描述:    "—§R无法建造§Y%building_bureaucratic_1%§!§!\n—能建造 £building£ §Y%building_information_tower%§!，提高%mod_planet_jobs_unity_produces_mult%，并随着星球首都的升级不断增加主流思潮吸引力、£amenities£舒适度、£trade_value£贸易额和%mod_planet_pops_consumer_goods_upkeep_mult%。"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "技术主义"
- -  "机械主义"

- text:    "是一定程度的§Y%ethic_fanatic_materialist%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   15
- 修正:=>- - 因子:   2
- - 拥有思潮:    "机械主义"
## <span title=civic_aristocratic_elite style="border-bottom:1px dotted"> "§H§Y世袭贵族§!§!"</span>
- 描述:    "—£building£ §Y首府建筑§!会替换部分 £job_politician£ §Y%job_politician%§!岗位为 £job_noble£ §Y%job_noble_plural%§!岗位.\n—被雇佣的§Y领袖§!不再需要花费£unity£ 凝聚力来维护.\n—§Y领袖§!有§Y20%§!几率初始自带额外的正面及负面特质各一个."
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "精英主义"
- -  "权威主义"

- text:    "是一定程度的§Y%ethic_fanatic_authoritarian%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   60
- 修正:=>- - 因子:   0
- - has_civic:   civic_empty_vagrant
- - NOR:=>- has_origin:   origin_ev_both_choosen
- has_civic:   civic_ev_planet_and_fleet
- has_ascension_perk:   ev_land_planets
- 修正:=>- - leaders_cost_mult:   -0.25
- - country_subject_power_penalty_mult:   0.25
- - planet_jobs_slave_produces_mult:   0.25
- - pop_ethic_authoritarian_attraction_mult:   0.25
- leader_background_job_weight:=>- noble:   200
## <span title=civic_nationalistic_zeal style="border-bottom:1px dotted">1 "征服者"</span>
- 随机权重:=>- 基础:   30
- 描述:    "—每摧毁一支敌军舰队，则%pop_citizen_happiness%§G+15%§!，持续一年。\n—每当自己的一支舰队被摧毁，则%pop_citizen_happiness%§R-15%§!，持续一年。"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "精英主义"
- -  "权威主义"
- -  "单一主义"
- -  "排外主义"

- text:   civic_tooltip_authoritarian_or_xenophobe
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - diplo_weight_naval_mult:   0.15
- - country_war_exhaustion_mult:   -0.25
- - country_claim_influence_cost_mult:   -0.2
- - country_border_friction_mult:   0.33
## <span title=civic_cyber_demos_cratos style="border-bottom:1px dotted"> "§H§Y网络民主§!§!"</span>
- 随机权重:=>- 基础:   60
- 修正:=>- - 因子:   0
- - has_civic:   civic_empty_vagrant
- - NOR:=>- has_origin:   origin_ev_both_choosen
- has_civic:   civic_ev_planet_and_fleet
- has_ascension_perk:   ev_land_planets
- 描述:    "—£building£ §Y首府建筑§!会替换部分 £job_politician£ §Y%job_politician%§!岗位为 £job_head_researcher£ §Y%job_head_researcher_plural%§!\n—解锁['concept_unique_technology']：%civic_OGAS%\n—£happiness£ %MOD_POP_HAPPINESS%高于§Y50§!的£pops£ 人口§G+1§!£stability£ %mod_planet_stability_mult%，£happiness£ %MOD_POP_HAPPINESS%低于§Y50§!的£pops£ 人口§R-1§!£stability£ %mod_planet_stability_mult%\n—开始游戏时解锁§Y%tech_administrative_ai%§!科技"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "技术主义"
- -  "机械主义"

- text:    "是一定程度的§Y%ethic_fanatic_materialist%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - category_computing_research_speed_mult:   0.25
- - planet_crime_mult:   0.3
- - pop_factions_unity_produces_add:   0.25
- - pop_ethic_materialist_attraction_mult:   0.25
## <span title=civic_indentured_assets style="border-bottom:1px dotted">civic_indentured_assets</span>
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "精英主义"
- -  "权威主义"

- text:    "是一定程度的§Y%ethic_fanatic_authoritarian%§!"
- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- 修正:=>- - planet_jobs_slave_produces_mult:   0.15
- - slave_market_cost_mult:   -0.15
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   5
- - 拥有思潮:    "排外主义"
## <span title=civic_evangelism style="border-bottom:1px dotted"> "福音传道"</span>
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "精神主义"
- -  "教权主义"

- text:    "是一定程度的§Y%ethic_fanatic_spiritualist%§!"
- 修正:=>- - country_trust_growth:   0.5
- - diplo_weight_pops_mult:   0.15
- - country_trust_cap_add:   50
- - diplo_weight_delegate_mult:   0.15
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   15
- 修正:=>- - 因子:   2
- - 拥有思潮:    "教权主义"
## <span title=civic_super_fast_paced_life style="border-bottom:1px dotted"> "超节奏生活"</span>
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   5
- - 拥有思潮:    "权威主义"
- 描述:    "—§Y%pop_cat_worker%§!阶级额外产出§Y0.25§!£trade_value£ %TRADE_VALUE%\n—§Y%pop_cat_specialist%§!阶级额外产出§Y0.75§!£trade_value£ %TRADE_VALUE%\n—§Y%pop_cat_ruler%§!阶级额外产出§Y1.75§!£trade_value£ %TRADE_VALUE%\n—§Y市场经济§!下, 无经济危机时, 提供§Y+0.3§!%economic_situation_improve%。"
- 需求:=>- 思潮:=>- value:    "个人主义"
- NOR:=>- value:
- -  "精神主义"
- -  "教权主义"

- text:    "不接受任何程度的§Y教权主义§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - planet_pops_consumer_goods_upkeep_mult:   0.1
- - planet_pops_organics_food_upkeep_mult:   0.1
- - pop_ethic_capitalism_attraction_mult:   0.15
- - planet_pops_minerals_upkeep_mult:   0.1
- - pop_growth_speed_reduction:   0.2
- - pop_lifestyle_trade_mult:   0.5
## <span title=civic_proletarian_culture style="border-bottom:1px dotted"> "劳动与文化"</span>
- 描述:    "—将 £building£ §Y%building_holo_theatres%§!替换为§Y%building_cultural_palace%§!\n—£job_entertainer£ %job_entertainer_plural%额外产出§Y1§!£unity£ %unity%并不再消耗£consumer_goods£ %consumer_goods%，但提供的£mod_planet_amenities_add£ %PLANET_AMENITIES_TITLE%§R-2§!"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "合作主义"
- -  "集体主义"

- text:    "是一定程度的§Y%ethic_fanatic_socialism%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- hide_modifiers:   yes
- 随机权重:=>- 基础:   10
- 修正:=>- - 因子:   5
- - 拥有思潮:    "集体主义"
- 修正:=>- - planet_entertainers_unity_produces_add:   1
- - planet_entertainers_consumer_goods_upkeep_add:   -1
- swap_type:=>- 描述:    "—将 £building£ §Y%building_holo_theatres%§!替换为§Y%building_cultural_palace%§!\n—£job_duelist£ %job_duelist_plural%额外产出§Y1§!£unity£ %unity%并不再消耗£alloys£ %alloys%，但提供的£mod_planet_amenities_add£ %PLANET_AMENITIES_TITLE%§R-2§!"
- trigger:=>- is_duelist_country:   yes
## <span title=civic_gospel_of_the_masses style="border-bottom:1px dotted">civic_gospel_of_the_masses</span>
- 描述:   civic_tooltip_gospel_of_the_masses_effects
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "精神主义"
- -  "教权主义"

- text:    "是一定程度的§Y%ethic_fanatic_spiritualist%§!"
- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- 修正:=>- - pop_ethic_spiritualist_attraction_mult:   0.5
- - pop_citizen_happiness:   0.1
- 随机权重:=>- 基础:   25
## <span title=civic_machine_introspective style="border-bottom:1px dotted">civic_machine_introspective</span>
- 随机权重:=>- 基础:   5
- 前置条件:=>- 政体:=>- value:   auth_machine_intelligence
- 修正:=>- - country_engineering_tech_research_speed:   0.2
- - intel_encryption_add:   1
- - councilor_gestalt_cognitive_exp_gain:   @gestalt_civic_node_xp_rate
- - country_physics_tech_research_speed:   0.15
- - scientist_initial_skill:   2
## <span title=civic_hive_devouring_swarm style="border-bottom:1px dotted">civic_hive_devouring_swarm</span>
- modification:=>- add:=>- has_tradition:    "未来传统完成"
- has_technology:   tech_ascension_theory
- 描述:   civic_tooltip_devouring_swarm_effects
- 需求:=>- origin:=>- NOR:=>- value:
- - origin_common_ground
- - origin_hegemon
- - origin_tree_of_life

- 前置条件:=>- 政体:=>- value:   auth_hive_mind
- 随机权重:=>- 基础:   5
- 修正:=>- - ship_hull_regen_add_perc:   0.05
- - councilor_gestalt_legion_exp_gain:   @gestalt_civic_node_xp_rate
- - country_starbase_influence_cost_mult:   -0.5
- - category_biology_research_speed_mult:   0.2
- - army_damage_mult:   0.8
- - starbase_shipyard_build_cost_mult:   -0.35
- - ship_hull_mult:   0.5
- - ship_armor_regen_add_perc:   0.05
- - country_naval_cap_mult:   1
- swap_type:=>- 描述:   civic_tooltip_devouring_swarm_lithoid_effects
- name:   civic_hive_devouring_swarm_lithoid
- trigger:=>- local_human_species_class:   LITHOID
## <span title=civic_exalted_priesthood style="border-bottom:1px dotted"> "§H§Y神权政治§!§!"</span>
- 随机权重:=>- 基础:   60
- 修正:=>- - 因子:   0
- - has_civic:   civic_empty_vagrant
- - NOR:=>- has_origin:   origin_ev_both_choosen
- has_civic:   civic_ev_planet_and_fleet
- has_ascension_perk:   ev_land_planets
- 描述:    "—£building£ §Y首都建筑§!会替换部分 £job_politician£ §Y%job_politician%§!岗位为 £job_high_priest£ §Y%job_high_priest_plural%§!\n—£job_priest£ %job_priest_plural%会额外产出§Y1§! £stability£ %PLANET_STABILITY_TITLE%并减少§Y%MOD_SPECIES_EMPIRE_SIZE_MULT%§!\n—£pop£ §Y唯心主义人口§!将会减少星球上的§Y%MOD_POP_AMENITIES_USAGE_MULT%§!\n—§Y%official%§!初始等级§G+2§!"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "精神主义"
- -  "教权主义"

- text:    "是一定程度的§Y%ethic_fanatic_spiritualist%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - planet_stability_add:   5
- - country_physics_tech_research_speed:   -0.05
- - empire_size_pops_mult:   -0.2
- - pop_ethic_spiritualist_attraction_mult:   0.25
## <span title=civic_hive_extremely_efficient_storage style="border-bottom:1px dotted"> "%civic_extremely_efficient_storage%"</span>
- 描述:    "—§Y%building_resource_silo%§!行星建筑额外§G+5000§!%MOD_COUNTRY_RESOURCE_MAX_ADD%，提高星球%MOD_PLANET_AMENITIES_MULT%并§G+1§!£job_warrior_drone£ %job_warrior_drone_plural%岗位\n—§Y%building_resource_silo%§!恒星基地建筑额外§G+5000§!%MOD_COUNTRY_RESOURCE_MAX_ADD%，并§G+1§!£unity£ %unity%\n—£building£§Y首都建筑§!提供的%MOD_COUNTRY_RESOURCE_MAX_ADD%翻倍"
- alternate_civic_version:    "极效仓储"
- 前置条件:=>- 政体:=>- value:   auth_hive_mind
- 修正:=>- - country_resource_max_minor_artifacts_add:   2500
- - country_resource_max_astral_threads_add:   250
- 随机权重:=>- 基础:   5
## <span title=civic_hive_warpdrive_start style="border-bottom:1px dotted"> "%civic_warpdrive_start%"</span>
- modification:=>- add:=>- has_tradition:    "未来科技"
- 描述:   civic_tooltip_warpdrive_start_effects
- alternate_civic_version:    "超越光芒"
- 前置条件:=>- 政体:=>- value:   auth_hive_mind
- 需求:=>- civics:=>- NOR:=>- value:
- - civic_eager_explorers
- -  "私人航空集团"
- - civic_hive_stargazers
- - civic_machine_exploration_protocol
- -  "§E§H原始密教§!§!"

- 修正:=>- - country_starbase_influence_cost_mult:   -0.25
- - country_starbase_influence_cost_distance_mult:   -0.33
- 随机权重:=>- 基础:   5
## <span title=civic_asceticism style="border-bottom:1px dotted"> "禁欲主义"</span>
- 随机权重:=>- 基础:   10
- 修正:=>- - 因子:   2.5
- - 拥有思潮:    "道德主义"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "精神主义"
- -  "教权主义"

- text:    "是一定程度的§Y%ethic_fanatic_spiritualist%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - planet_pops_consumer_goods_upkeep_mult:   -0.2
- - pop_growth_speed:   -0.1
- - planet_pops_organics_food_upkeep_mult:   -0.2
- - pop_amenities_usage_mult:   -0.1
- - planet_pops_organics_minerals_upkeep_mult:   -0.2
- - pop_happiness:   -0.15
## <span title=civic_machine_hyperspace_specialty style="border-bottom:1px dotted">"同调加速"</span>
- ai_playable:=>- has_astral_planes_dlc:   yes
- 描述:   civic_machine_hyperspace_specialty_effects
- playable:=>- has_astral_planes_dlc:   yes
- 需求:=>- civics:=>- NOT:=>- value:   civic_machine_exploration_protocol
- 前置条件:=>- 政体:=>- value:   auth_machine_intelligence
- 修正:=>- - ship_speed_mult:   0.1
- - planet_sensor_range_add:   2
- - country_physics_tech_research_speed:   0.15
## <span title=civic_eager_explorers style="border-bottom:1px dotted">civic_eager_explorers</span>
- modification:=>- add:=>- has_technology:   tech_subspace_drive
- 描述:   civic_eager_explorers_effects
- playable:=>- has_first_contact_dlc:   yes
- 需求:=>- origin:=>- NOR:=>- value:
- -  "厚积薄发"
- -  "异星歧途"
- - origin_payback
- - origin_broken_shackles
- - origin_fear_of_the_dark

- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   0
## <span title=civic_glorious_pioneer style="border-bottom:1px dotted"> "§H§Y思想设计师§!§!"</span>
- 随机权重:=>- 基础:   50
- 修正:=>- - 因子:   0
- - has_civic:   civic_empty_vagrant
- - NOR:=>- has_origin:   origin_ev_both_choosen
- has_civic:   civic_ev_planet_and_fleet
- has_ascension_perk:   ev_land_planets
- 描述:    "—£building£ §Y首都建筑§!会替换部分 £job_politician£ §Y%job_politician%§!岗位为 £job_core_party_members£ §Y%job_core_party_members_plural%§!\n—§Y%pop_cat_ruler%§!阶级额外产出§Y2§! £unity£ 凝聚力\n—§Y奴隶§!人口额外产出§Y1§!£minerals£ %minerals%与£energy£ %energy%\n—不能使用§Y%trade_policy_unity%§!税收投资政策"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "合作主义"
- -  "集体主义"

- text:    "是一定程度的§Y%ethic_fanatic_socialism%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - leaders_cost_mult:   0.25
- - country_base_influence_produces_add:   1
- - country_pop_enslaved_mult:   0.25
- - pop_ethic_authoritarian_attraction_mult:   0.25
## <span title=civic_hive_divided_attention style="border-bottom:1px dotted">civic_hive_divided_attention</span>
- 随机权重:=>- 基础:   5
- 需求:=>- civics:=>- NOR:=>- value:   civic_hive_one_mind
- 前置条件:=>- 政体:=>- value:   auth_hive_mind
- 修正:=>- - councilor_gestalt_growth_exp_gain:   @gestalt_civic_node_xp_rate
- - country_admin_cap_mult:   0.2
- - empire_size_colonies_mult:   -0.33
## <span title=civic_labour_unions style="border-bottom:1px dotted"> "企业工会"</span>
- 需求:=>- 思潮:=>- NOR:=>- value:
- -  "精英主义"
- -  "权威主义"
- -  "个人主义"

- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- 修正:=>- - pop_cat_worker_happiness:   0.1
- - planet_jobs_worker_produces_mult:   0.05
- - pop_cat_worker_political_power:   1
- 随机权重:=>- 基础:   10
- 修正:=>- - 因子:   2.5
- - 拥有思潮:    "集体主义"
## <span title=civic_military_dictatorship style="border-bottom:1px dotted"> "§H§Y战争领主§!§!"</span>
- 描述:    "—£building£ §Y首都建筑§!会替换部分 £job_politician£ §Y%job_politician%§!岗位为 £job_knight_commander£ §Y%job_knight_commander_plural%§!。\n—£job_soldier£ §Y%job_soldier_plural%§!额外提高§Y2.5§! £stability£ %PLANET_STABILITY_TITLE%。\n—每个§Y%opinion_is_subject%§!将强化我们的军事实力。\n—新的§Y%ruler_with_icon%§!登基后允许花费大量资源建造一艘§Y超级战舰§!。"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "干涉主义"
- -  "军国主义"

- text:    "是一定程度的§Y%ethic_fanatic_militarist%§!"
- can_build_ruler_ship:   yes
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   60
- 修正:=>- - 因子:   0
- - has_civic:   civic_empty_vagrant
- - NOR:=>- has_origin:   origin_ev_both_choosen
- has_civic:   civic_ev_planet_and_fleet
- has_ascension_perk:   ev_land_planets
- 修正:=>- - country_naval_capacity_contribution_from_subjects_mult:   0.33
- - country_enclave_capacity_add:   2
- - empire_size_penalty_mult:   0.25
- - pop_ethic_militarist_attraction_mult:   0.25
## <span title=civic_natural_design style="border-bottom:1px dotted"> "血肉崇拜"</span>
- modification:   no
- 描述:    "—开始游戏时就能§G成为完美的生物体§!。\n—%AVAILABLE_BUILDINGS%['concept_transcendental_retreat']\n—能够§R“净化”§!星球上的§B机器人口§!与§E义体人口§!，每个被净化人口将产出0.5%r_unity%与1%r_energy%。"
- AI_weight:=>- 基础:   10
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "单一主义"
- -  "排外主义"

- text:    "是一定程度的§Y%ethic_fanatic_xenophobe%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- negative_description:   "—§R警告：禁用所有飞升路线！§!\n—§R警告：无法修饰有机物种！§!\n—当境内拥有§B机器人口§!或§E义体人口§!时，星球幸福度减少。\n—降低对已经开始§Y飞升路线§!的帝国的赞同度"
- 修正:=>- - BIOLOGICAL_species_trait_picks_add:   5
- - BIOLOGICAL_species_trait_points_add:   15
- - planet_researchers_society_research_produces_add:   0.33
- traits:=>- trait:
- - trait_latent_psionic
- - trait_erudite
- - trait_fertile
- - trait_robust

- leader_background_job_weight:=>- healthcare:   100
## <span title=civic_selective_kinship style="border-bottom:1px dotted">"选择性亲缘"</span>
- 描述:
- - civic_selective_kinship
- - civic_tooltip_selective_kinship_effects

- ai_playable:=>- has_lithoids:   yes
- playable:=>- has_lithoids:   yes
- 需求:=>- 思潮:=>- NOR:=>- value:
- -  "多元主义"
- -  "崇外主义"
- -  "自由主义"

- text:    "不接受任何程度的§Y崇外主义§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   4
- 修正:=>- - citizen_pop_same_species_class_happiness:   0.075
- - citizen_pop_different_species_class_happiness:   0.025
## <span title=civic_galactic_sovereign_people style="border-bottom:1px dotted"> "共产星际"</span>
- modification:   no
- 描述:    "—银河帝国内的所有国家将受到§Y革命宣传§!的影响"
- 前置条件:=>- civics:=>- value:    "共产星际"
- icon:   gfx/interface/icons/governments/civics/civic_galactic_sovereign.dds
- 随机权重:=>- 基础:   0
- 修正:=>- - envoys_add:   1
- - diplo_weight_mult:   0.4
- - country_base_influence_produces_add:   6
- - country_government_civic_points_add:   1
## <span title=civic_hive_empath style="border-bottom:1px dotted">civic_hive_empath</span>
- 描述:   civic_tooltip_empath_effects
- playable:=>- host_has_dlc:   Federations
- 需求:=>- civics:=>- NOT:=>- value:   civic_hive_devouring_swarm
- 前置条件:=>- 政体:=>- value:   auth_hive_mind
- 修正:=>- - councilor_gestalt_growth_exp_gain:   @gestalt_civic_node_xp_rate
- - diplo_weight_mult:   0.2
- - envoys_add:   2
- - country_trust_growth:   0.3
## <span title=civic_corporate_honorary_curator style="border-bottom:1px dotted"> "银河展销会"</span>
- 描述:    "—提高§H非灭绝§!国家对你的评价\n—相邻的国家§G+10%§!%TRADE_VALUE%\n—§Y市场经济§!下, 无经济危机时, 提供§Y+0.1§!%economic_situation_improve%和§Y+40§!%economic_crisis_threshold%。"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "和平主义"
- -  "道德主义"

- text:    "是一定程度的§Y%ethic_fanatic_pacifist%§!"
- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- 修正:=>- - add_base_country_intel:   20
- - diplo_weight_mult:   0.25
- - planet_jobs_specialist_produces_mult:   0.1
- - country_energy_produces_mult:   -0.1
- 随机权重:=>- 基础:   25
- 修正:=>- - 因子:   1.5
- - 拥有思潮:    "崇外主义"
## <span title=civic_peace_defense_forces style="border-bottom:1px dotted"> "和平防卫军"</span>
- 描述:   civic_tooltip_peace_defense_forces_effects
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "和平主义"
- -  "道德主义"

- text:    "是一定程度的§Y%ethic_fanatic_pacifist%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - damage_vs_country_type_swarm_mult:   0.25
- - damage_vs_country_type_ai_empire_mult:   0.25
- - damage_vs_country_type_extradimensional_mult:   0.25
- - damage_vs_country_type_gray_mult:   0.25
- - damage_vs_country_type_extradimensional_2_mult:   0.25
- - damage_vs_country_type_extradimensional_3_mult:   0.25
- - damage_vs_player_crisis_mult:   0.25
- 随机权重:=>- 基础:   5
## <span title=civic_zhaowen_dao style="border-bottom:1px dotted"> "朝闻道"</span>
- 描述:    "—每隔一段时间都会有科学家献身\n—§Y人口§!额外生产 §Y0.25§! £physics£ £society£ £engineering£ 研究点数\n—§R禁忌的研究将有几率导致宇宙运行的崩溃，随着时间推移，这一几率会越来越大§!\n—£job_head_researcher£ §Y%job_head_researcher_plural%§!提供额外的£unity£ §Y%unity%§!"
- 需求:=>- 思潮:=>- value:    "机械主义"
- NOT:=>- value:    "道德主义"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - planet_researchers_unity_produces_add:   2
- - pop_growth_speed_reduction:   0.25
- 随机权重:=>- 基础:   0
## <span title=civic_debug style="border-bottom:1px dotted">civic_debug</span>
- modification:   no
- 前置条件:=>- civics:=>- value:   civic_debug
- 随机权重:=>- 基础:   0
## <span title=civic_democracy_and_clean_government style="border-bottom:1px dotted"> "民主廉政"</span>
- 随机权重:=>- 基础:   10
- 修正:=>- - 因子:   0
- - is_species_class:   HUM
- 描述:    "—替换 £job_bureaucrat£ §Y%job_bureaucrat_plural%§!岗位为 £job_clerk£ §Y%job_clerk%§!岗位， £job_clerk£ §Y%job_clerk%§!额外产出少量的§Y%MOD_COUNTRY_ADMIN_CAP_ADD%§!\n—§R%civic_anarchism%§!也能够建造§Y%building_bureaucratic_1%§!\n—§Y%civic_peaceful_republic%§!与§Y%civic_executive_committee%§!对 £job_bureaucrat£ §Y%job_bureaucrat_plural%§!的加成同样应用于 £job_clerk£ §Y%job_clerk%§!\n—开始游戏时解锁§Y%tech_effective_bureaucracy%§!科技"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "宪政主义"
- -  "自由主义"

- text:    "是一定程度的§Y%ethic_fanatic_egalitarian%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - empire_size_penalty_mult:   -0.10
## <span title=civic_primitive_worship style="border-bottom:1px dotted"> "§E§H原始密教§!§!"</span>
- 描述:   civic_tooltip_primitive_worship_effects
- 需求:=>- 思潮:=>- value:    "教权主义"
- NOT:=>- value:    "个人主义"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - farming_district_housing_add:   3
- - pop_growth_speed_reduction:   1
- - planet_pops_consumer_goods_upkeep_mult:   -9.99
- - pop_ethic_spiritualist_attraction_mult:   0.5
- - planet_jobs_consumer_goods_upkeep_mult:   -9.99
- - pop_growth_speed:   1
- - job_primitive_artisan_per_pop:   0.05
- - farming_district_buildings_add:   1
- - job_priest_per_pop:   0.05
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   0
- - has_civic:   civic_empty_vagrant
- - NOR:=>- has_origin:   origin_ev_both_choosen
- has_civic:   civic_ev_planet_and_fleet
- has_ascension_perk:   ev_land_planets
## <span title=civic_sparta_spirit style="border-bottom:1px dotted"> "§E§H伟大军国§!§!"</span>
- 描述:    "—能够无视思潮与国策的限制使用奴隶制。\n—§Y公民§!人口仅能担任£pop_cat_ruler£ §Y%pop_cat_ruler_plural%§!、£job_soldier£§Y军事类§!、£job_enforcer£§Y执法类§!、和£job_researcher£ £job_bureaucrat£§Y复杂专家§!岗位，失业的公民人口会自动成为无上限的£job_conscript_uncapped£ §Y%job_conscript_uncapped_plural%§!。\n—专注于军事研究的£job_researcher£§Y%job_researcher_plural%§!将会使用%r_alloys%产出更多%r_physics%和%r_engineering%。\n—§Y奴隶§!人口能且只能担任以上岗位以外的非军事岗位，§Y%citizenship_limited%§!的人口可以担任全部非£pop_cat_ruler£ §Y%pop_cat_ruler_plural%§!岗位，工作产生的%r_alloys%和%r_consumer_goods%产出提高§G10%§!，但£happiness£ 幸福度额外降低§R10%§!，且禁止§Y%slavery_military%§!奴役方式。\n—替换£job_entertainer£ §Y%job_entertainer%§!岗位为£job_duelist£ §Y%job_duelist%§!岗位，替换£building£ §Y%building_autochthon_monument%§!提供的£job_culture_worker£ §Y%job_culture_worker%§!岗位为£job_commandante£ §Y%job_commandante%§!岗位\n—£job_commandante£ §Y%job_commandante_plural%§!岗位会提高%MOD_SHIP_WEAPON_RANGE_MULT%，£job_soldier£ §Y%job_soldier_plural%§!岗位会提高%MOD_SHIP_FIRE_RATE_MULT%，£job_conscript_uncapped£ §Y%job_conscript_uncapped_plural%§!会提高%MOD_SHIP_HULL_MULT%。\n—开始游戏时解锁§Y集中指挥§!科技。\n—绝大多数政策只能选择§Y军国主义§!选项。"
- 需求:=>- 思潮:=>- value:    "军国主义"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   0
- - has_civic:   civic_empty_vagrant
- - NOR:=>- has_origin:   origin_ev_both_choosen
- has_civic:   civic_ev_planet_and_fleet
- has_ascension_perk:   ev_land_planets
- 修正:=>- - pop_demotion_time_mult:   -1
- - ship_starting_experience_add:   10000
- - pop_ethic_militarist_attraction_mult:   1
- - army_starting_experience_add:   10000
- - country_war_exhaustion_mult:   -0.75
- - planet_jobs_slave_produces_mult:   0.25
- custom_tooltip_with_modifiers:   civic_sparta_spirit_effects_additional
- leader_background_job_weight:=>- conscript_uncapped:   100
## <span title=civic_procrastination style="border-bottom:1px dotted"> "后发先至"</span>
- modification:   no
- 描述:    "—开始游戏时无效果，之后每过§Y20§!年便有一次选择的机会，可选择保留该['concept_national_culture']或是移除该['concept_national_culture']以换取额外的%MOD_COUNTRY_GOVERNMENT_CIVIC_POINTS_ADD%。每一次选择保留则下一次可换取的%MOD_COUNTRY_GOVERNMENT_CIVIC_POINTS_ADD%§G+1§!，上限§Y10§!个。"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   1
- 修正:=>- - 因子:   0
- - OR:=>- has_origin:
- -  "厚积薄发"
- -  "异星歧途"

## <span title=civic_technocracy style="border-bottom:1px dotted"> "§H§Y技术治国§!§!"</span>
- 随机权重:=>- 基础:   60
- 修正:=>- - 因子:   0
- - has_civic:   civic_empty_vagrant
- - NOR:=>- has_origin:   origin_ev_both_choosen
- has_civic:   civic_ev_planet_and_fleet
- has_ascension_perk:   ev_land_planets
- 描述:   civic_tooltip_technocracy_effects
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "技术主义"
- -  "机械主义"

- text:    "是一定程度的§Y%ethic_fanatic_materialist%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - scientist_initial_skill:   2
- - pop_factions_produces_mult:   -0.15
- - planet_crime_mult:   -0.2
- - pop_ethic_materialist_attraction_mult:   0.25
## <span title=civic_machine_sovereign_guardianship style="border-bottom:1px dotted">civic_machine_sovereign_guardianship</span>
- ai_playable:=>- has_astral_planes_dlc:   yes
- 描述:   civic_machine_sovereign_guardianship_effects
- playable:=>- has_astral_planes_dlc:   yes
- 需求:=>- civics:=>- NOT:=>- value:   civic_machine_terminator
- 前置条件:=>- 政体:=>- value:   auth_machine_intelligence
- 随机权重:=>- 基础:   @civic_rare_random_weight
- 修正:=>- - starbase_defense_platform_capacity_add:   3
- - planet_orbital_bombardment_damage:   -0.25
- - country_border_friction_mult:   -0.15
- - army_defense_health_mult:   0.15
- - empire_size_systems_mult:   1
- ai_weight:=>- 基础:   @civic_rare_random_weight
## <span title=civic_righteous_fury style="border-bottom:1px dotted"> "正义之怒"</span>
- 描述:   civic_tooltip_righteous_fury_effects
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "宪政主义"
- -  "自由主义"

- text:    "是一定程度的§Y%ethic_fanatic_egalitarian%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   5
## <span title=civic_shared_burden style="border-bottom:1px dotted">1 "§H§Y劳动民主§!§!"</span>
- 描述:    "—£building£ §Y首都建筑§!会替换部分 £job_politician£ §Y%job_politician%§!岗位为 £job_labour_hero£ §Y%job_labour_hero%§!\n—£job_labour_hero£ §Y%job_labour_hero%§!额外产出§Y2§!£physics_research£ £engineering_research£ £society_research£ 研究点数，但额外消耗§Y1§!£consumer_goods£ 消费品\n—§Y%pop_cat_worker%§!阶级额外产出§Y0.25§!£unity£ 凝聚力，同时根据不同的职业分别产出§Y0.25§!£physics_research£ 物理学研究、£engineering_research£ 工程学研究或£society_research£ 社会学研究，并额外消耗§Y0.15§!£consumer_goods£ 消费品\n—可采用§Y%living_standard_utopian%§!生活标准，无论其所属§Y阶层§!，在该标准下所有£pop£ 人口拥有丰富的£consumer_goods£ §Y%consumer_goods%§!维护费并享有同等§Y政治权力§!。"
- swap_type:=>- 描述:   civic_tooltip_communist_society_effects
- trigger:=>- has_tradition:    "未来社会"
- has_technology:   tech_ascension_theory
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "合作主义"
- -  "集体主义"

- text:    "是一定程度的§Y%ethic_fanatic_socialism%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- leader_background_job_weight:=>- "farmer":   25
- "labour_hero":   50
- "technician":   25
- "miner":   25
- 修正:=>- - pop_cat_worker_happiness:   0.1
- - pop_demotion_time_mult:   -1
- - planet_pops_unemployed_consumer_goods_upkeep_add:   1
- - pop_ethic_socialism_attraction_mult:   0.25
- 随机权重:=>- 基础:   100
- 修正:=>- - 因子:   0
- - has_civic:   civic_empty_vagrant
- - NOR:=>- has_origin:   origin_ev_both_choosen
- has_civic:   civic_ev_planet_and_fleet
- has_ascension_perk:   ev_land_planets
## <span title=civic_toxic_baths_individual_machine style="border-bottom:1px dotted">civic_toxic_baths_individual_machine</span>
- modification:=>- add:=>- has_tradition:    "未来科技"
- playable:=>- has_toxoids:   yes
- alternate_civic_version:    "诱变水疗中心"
- ai_playable:=>- has_toxoids:   yes
- 描述:   civic_tooltip_machine_toxic_baths_effects
- 需求:=>- origin:=>- NOT:=>- value:   origin_life_seeded
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- icon:   gfx/interface/icons/governments/civics/civic_toxic_baths.dds
- 随机权重:=>- 基础:   @civic_uncommon_random_weight
- ai_weight:=>- 基础:   @ai_civic_uncommon_base_weight
- 修正:=>- - 因子:   @ai_civic_personality_mismatch_factor
- - OR:=>- has_ai_personality:
- - democratic_crusaders
- - honorbound_warriors
- - evangelising_zealots

## <span title=civic_declaration_of_human_rights style="border-bottom:1px dotted"> "人权宣言"</span>
- 需求:=>- 思潮:=>- value:    "自由主义"
- NOR:=>- value:
- -  "单一主义"
- -  "排外主义"

- text:    "不接受任何程度的§Y排外主义§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - country_pop_enslaved_mult:   -1
- - pop_cat_slave_happiness:   1
- 随机权重:=>- 基础:   1
- 修正:=>- - 因子:   50
- - has_civic:    "§E§H三倍利润§!§!"
- - 拥有思潮:    "自由主义"
## <span title=civic_independent style="border-bottom:1px dotted"> "平等独立"</span>
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "合作主义"
- -  "集体主义"

- text:    "是一定程度的§Y%ethic_fanatic_socialism%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - intel_encryption_add:   2
- - starbase_defensive_war_ship_build_speed_mult:   0.25
- - army_defense_morale_mult:   0.5
- - pop_government_ethic_attraction:   0.2
- - country_hostile_claim_influence_cost_mult:   0.25
- - country_border_friction_mult:   0.25
- 随机权重:=>- 基础:   15
- 修正:=>- - 因子:   2
- - 拥有思潮:    "单一主义"
## <span title=civic_spy_agency style="border-bottom:1px dotted"> "间谍机关"</span>
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   5
- - 拥有思潮:    "排外主义"
- 需求:=>- 思潮:=>- NOR:=>- value:    "崇外主义"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - ship_cloaking_detection_add:   2
- - add_base_country_intel:   30
- - intel_decryption_add:   2
- - espionage_operation_cost_mult:   -0.25
- - spy_network_daily_value_mult:   0.25
## <span title=civic_curse_of_blood_kin style="border-bottom:1px dotted"> "血源诅咒"</span>
- 描述:    "—人口将额外提高§G%mod_planet_jobs_produces_mult%§!与§R%MOD_POP_GROWTH_SPEED_REDUCTION%§!。\n—§Y领袖§!开始将随机获得一系列的§Y心理特质§!。\n—开始游戏时解锁§Y%tech_selected_lineages%§!科技。"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "精英主义"
- -  "权威主义"

- text:    "是一定程度的§Y%ethic_fanatic_authoritarian%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - pop_cat_specialist_happiness:   -0.05
- - species_leader_exp_gain:   0.1
- - pop_cat_worker_happiness:   -0.1
- 随机权重:=>- 基础:   15
- 修正:=>- - 因子:   3
- - 拥有思潮:    "权威主义"
## <span title=civic_mining_guilds style="border-bottom:1px dotted">civic_mining_guilds</span>
- 随机权重:=>- 基础:   10
- 修正:=>- - 因子:   5
- - is_species_class:   LITHOID
- 描述:    "—£job_miner£ §Y%job_miner_plural%§!同时产出§G2§! £amenities£ 舒适度和§Y3§! £trade_value£ 贸易额"
- 需求:=>- civics:=>- NOR:=>- value:
- -  "自然卫士"
- - 1 "田园牧歌"
- -  "无情工业化"

- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - mining_district_housing_add:   2
- - mining_district_buildings_add:   0.34
- - planet_miners_minerals_produces_add:   1.5
## <span title=civic_military_industry style="border-bottom:1px dotted"> "战争工匠"</span>
- 随机权重:=>- 基础:   10
- 修正:=>- - 因子:   2.5
- - 拥有思潮:    "机械主义"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "技术主义"
- -  "机械主义"

- text:    "是一定程度的§Y%ethic_fanatic_materialist%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - ship_armor_mult:   0.2
- - ship_weapon_damage:   0.2
- - ship_weapon_range_mult:   0.2
- - category_propulsion_research_speed_mult:   0.33
- - starbase_shipyard_build_cost_mult:   0.15
## <span title=civic_Joker style="border-bottom:1px dotted"> "笑话"</span>
- 描述:   civic_Joker_effects
- 需求:=>- civics:=>- NOR:=>- value:
- - 1 "任人唯贤"
- -  "超人经济"

- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   5
## <span title=civic_machine_factory_overclock style="border-bottom:1px dotted">civic_machine_factory_overclock</span>
- icon:   gfx/interface/icons/governments/civics/civic_machine_factory_overclock.dds
- 随机权重:=>- 基础:   5
- 前置条件:=>- 政体:=>- value:   auth_machine_intelligence
- 修正:=>- - councilor_gestalt_regulatory_exp_gain:   @gestalt_civic_node_xp_rate
- - leaders_cost_mult:   0.25
- - planet_jobs_specialist_produces_mult:   0.2
- - country_leader_cap_add:   1
- - leaders_upkeep_mult:   0.25
## <span title=civic_army_production style="border-bottom:1px dotted"> "耕战一体"</span>
- 描述:    "—£job_soldier£ §Y%job_soldier_plural%§!与£job_conscript£ §Y%job_conscript_plural%§!产出£food£ 食物与£alloys£ 合金，以及少量£minerals£ 矿物、£energy£ 能量和£unity£ 凝聚力\n—动员出的部队将无需§Y维护费§!"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "干涉主义"
- -  "军国主义"

- text:    "是一定程度的§Y%ethic_fanatic_militarist%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - job_soldier_add:   3
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   5
- - 拥有思潮:    "军国主义"
## <span title=civic_executive_committee style="border-bottom:1px dotted"> "§H§Y科举共和§!§!"</span>
- 描述:    "—£building£ §Y首都建筑§!会替换部分 £job_politician£ §Y%job_politician%§!岗位为 £job_supervisor£ §Y%job_supervisor_plural%§!。\n—§Y领袖§!有§Y25%§!几率初始自带一个额外的正面特质。\n—接受过良好教育的的£pop£ §Y人口§!将额外提高自己的专业技术水平。\n—§Y%official%§!初始等级§G+2§!。"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "和平主义"
- -  "道德主义"

- text:    "是一定程度的§Y%ethic_fanatic_pacifist%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   60
- 修正:=>- - 因子:   0
- - has_civic:   civic_empty_vagrant
- - NOR:=>- has_origin:   origin_ev_both_choosen
- has_civic:   civic_ev_planet_and_fleet
- has_ascension_perk:   ev_land_planets
- 修正:=>- - empire_size_pops_mult:   -0.50
- - species_leader_exp_gain:   1
- - planet_pops_upkeep_mult:   0.25
- - pop_ethic_pacifist_attraction_mult:   0.25
- leader_background_job_weight:=>- teacher:   500
## <span title=civic_machine_paradise_lost style="border-bottom:1px dotted"> "乐土机械"</span>
- 描述:    "—£building£ §Y%building_organic_sanctuary%§!与£building£ §Y%building_organic_paradise%§!将提供额外的£amenities£ %MOD_PLANET_AMENITIES_ADD%，并且每个£job_maintenance_drone£ §Y%job_maintenance_drone_plural%§!§G+1%§!%MOD_POP_HAPPINESS%\n—允许建造£building£ §Y%building_gaiaseeders%§!建筑\n—开始游戏时解锁§Y%tech_terrestrial_sculpting%§!与§Y%tech_paradise_dome%§!科技"
- 随机权重:=>- 基础:   5
- 需求:=>- civics:=>- NOT:=>- value:
- - origin_shattered_ring
- - origin_void_dwellers

- 前置条件:=>- OR:=>- 政体:=>- value:   auth_machine_intelligence
- 修正:=>- - councilor_gestalt_growth_exp_gain:   @gestalt_civic_node_xp_rate
## <span title=civic_moth_chasing_flames style="border-bottom:1px dotted"> "逐火之蛾"</span>
- 需求:=>- 思潮:=>- NOR:=>- value:
- -  "宪政主义"
- -  "自由主义"

- text:    "不接受任何程度的§Y自由主义§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - species_leader_exp_gain:   5
- - leader_lifespan_add:   -20
- - planet_jobs_produces_mult:   0.33
- - pop_growth_speed_reduction:   0.33
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   3
- - 拥有思潮:    "个人主义"
## <span title=civic_eternal_jihad style="border-bottom:1px dotted"> "无休之季"</span>
- 描述:    "—提供特殊岗位：£job_professional_star_fans£ §Y%job_professional_star_fans_plural%§!，%job_professional_star_fans_effect_desc%\n—寺庙建筑将£job_priest£ §Y%job_priest_plural%§!替换为£job_manager£ §Y%job_manager_plural%§!和£job_entertainer£ %job_entertainer_plural%\n—可以使用 £unity£ 凝聚力招募§H圣战者§!陆军，他们脆弱但攻击力强且士气高昂。\n—§Y市场经济§!下, 无经济危机时, 提供§Y+0.2§!%economic_situation_improve%。"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "精神主义"
- -  "教权主义"

- text:    "是一定程度的§Y%ethic_fanatic_spiritualist%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   10
- 修正:=>- - 因子:   5
- - 拥有思潮:    "个人主义"
- 修正:=>- - country_unity_produces_mult:   -0.1
- - job_professional_star_fans_per_pop:   0.04
- - pop_factions_unity_produces_add:   -0.25
- - country_power_projection_influence_produces_add:   0.5
- - pop_cat_ruler_political_power:   2
- swap_type:=>- 描述:    "—提供特殊岗位：£job_professional_star_fans£ §Y%job_professional_star_fans_plural%§!，%job_professional_star_fans_effect_desc%\n—寺庙建筑将£job_priest£ §Y%job_priest_plural%§!替换为£job_manager£ §Y%job_manager_plural%§!和£job_duelist£ %job_duelist_plural%\n—可以使用 £unity£ 凝聚力招募§H圣战者§!陆军，他们脆弱但攻击力强且士气高昂。\n—§Y市场经济§!下, 无经济危机时, 提供§Y+0.2§!%economic_situation_improve%。"
- name:    "无休之季"
- trigger:=>- is_duelist_country:   yes
## <span title=civic_information_warrior style="border-bottom:1px dotted"> "真名实姓"</span>
- 描述:    "—开始游戏时解锁§Y%tech_decryption_1%§!与§Y%tech_decryption_2%§!科技"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "单一主义"
- -  "排外主义"

- text:    "是一定程度的§Y%ethic_fanatic_xenophobe%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - ship_cloaking_detection_add:   2
- - trade_value_mult:   0.15
- - job_criminal_per_crime:   0.03
- 随机权重:=>- 基础:   10
- 修正:=>- - 因子:   2.5
- - 拥有思潮:    "个人主义"
## <span title=civic_xeno_militarist style="border-bottom:1px dotted"> "调停者"</span>
- 随机权重:=>- 基础:   30
- 描述:    "—§Y保障独立§!和§Y互不侵犯条约§!不需要影响力维护\n—§Y防御条约§!将提供%r_unity%产出\n—军事力量%RELATIVE_POWER_1%或%RELATIVE_POWER_2%的国家将对你产生额外好感\n—§Y霸权家§!派系对§Y解放战争§!战争政策给予支持\n—§Y轨道轰炸§!选项受限"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "干涉主义"
- -  "军国主义"

- text:    "是一定程度的§Y%ethic_fanatic_militarist%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - diplo_weight_naval_mult:   0.15
- - country_vassal_naval_capacity_contribution_mult:   0.33
- - country_subject_acceptance_add:   20
- - country_claim_influence_cost_mult:   0.33
## <span title=civic_distribution_on_demand style="border-bottom:1px dotted"> "§E§H空想时代§!§!"</span>
- modification:   no
- ai_playable:=>- always:   no
- 前置条件:=>- civics:=>- NOT:=>- value:   civic_empty_vagrant
- cost:   3
- 修正:=>- - planet_jobs_produces_mult:   999.99
- - planet_buildings_produces_mult:   999.99
- - starbase_shipyard_build_speed_mult:   99.99
- - planet_building_build_speed_mult:   99.99
- - megastructure_build_speed_mult:   99.99
- 随机权重:=>- 基础:   0
## <span title=civic_big_industrial_farming style="border-bottom:1px dotted"> "大工业农作"</span>
- 随机权重:=>- 基础:   5
- 修正:=>- - 拥有思潮:    "道德主义"
- - 因子:   5
- - OR:=>- 拥有思潮:
- -  "技术主义"
- -  "机械主义"

- 描述:    "—£job_farmer£ %job_farmer%额外产出§Y4§!£trade_value£ %TRADE_VALUE%并§G+1%§!%mod_pop_lifestyle_trade_mult%\n—§Y农业§!区划将提供更少的岗位"
- 需求:=>- species_archetype:=>- NOR:=>- value:
- - LITHOID
- - MACHINE

- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - planet_farmers_food_produces_add:   6
- - planet_farmers_energy_upkeep_add:   2
## <span title=civic_answer style="border-bottom:1px dotted"> "答案"</span>
- 随机权重:=>- 基础:   1
- modification:=>- add:=>- has_tradition:    "未来科技"
- has_technology:   tech_ascension_theory
- 描述:    "—当星球上的%POPULATION_BUTTON%、§H%BUILDINGS_TITLE%§!与§H%DISTRICTS%§!数量为§Y42§!时，%mod_planet_jobs_produces_mult%与%mod_planet_buildings_produces_mult%将分别提高§G42%§!。\n—每隔§Y42§!年，所有星球的%r_trade_value%都将提高§G42§!倍，持续一整年。"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
## <span title=civic_hive_sovereign_guardianship style="border-bottom:1px dotted">civic_hive_sovereign_guardianship</span>
- ai_playable:=>- has_astral_planes_dlc:   yes
- 描述:   civic_hive_sovereign_guardianship_effects
- playable:=>- has_astral_planes_dlc:   yes
- 需求:=>- civics:=>- NOT:=>- value:   civic_hive_devouring_swarm
- 前置条件:=>- 政体:=>- value:   auth_hive_mind
- 随机权重:=>- 基础:   @civic_rare_random_weight
- 修正:=>- - starbase_defense_platform_capacity_add:   3
- - planet_orbital_bombardment_damage:   -0.25
- - country_border_friction_mult:   -0.15
- - army_defense_health_mult:   0.15
- - empire_size_systems_mult:   1
- ai_weight:=>- 基础:   @civic_rare_random_weight
## <span title=civic_machine_memorialist style="border-bottom:1px dotted"> "逆熵协议"</span>
- 描述:   civic_tooltip_memorialist_gestalt_effects
- playable:=>- host_has_dlc:   NecroidsSpeciesPack
- 需求:=>- civics:=>- NOR:=>- value:
- - civic_machine_terminator
- - civic_machine_assimilator

- 前置条件:=>- 政体:=>- value:   auth_machine_intelligence
- 随机权重:=>- 基础:   5
- 修正:=>- - councilor_gestalt_cognitive_exp_gain:   @gestalt_civic_node_xp_rate
## <span title=civic_memory_vault_hive style="border-bottom:1px dotted">civic_memory_vault_hive</span>
- ai_playable:=>- host_has_dlc:   GalacticParagons
- 描述:   civic_tooltip_memory_vault_hive_effects
- playable:=>- host_has_dlc:   GalacticParagons
- 需求:=>- civics:=>- NOT:=>- value:   civic_memory_vault
- 前置条件:=>- 政体:=>- value:   auth_hive_mind
- 随机权重:=>- 基础:   4
- 修正:=>- - councilor_gestalt_cognitive_exp_gain:   @gestalt_civic_node_xp_rate
- - councilor_skill_add:   1
## <span title=civic_socialized_support style="border-bottom:1px dotted"> "社会化扶养"</span>
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "合作主义"
- -  "集体主义"

- text:    "是一定程度的§Y%ethic_fanatic_socialism%§!"
- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- 修正:=>- - pop_growth_speed:   0.3
- - planet_pops_consumer_goods_upkeep_mult:   0.15
- 随机权重:=>- 基础:   10
- 修正:=>- - 因子:   2.5
- - 拥有思潮:    "集体主义"
## <span title=civic_spirit_of_rule_by_man style="border-bottom:1px dotted"> "人治精神"</span>
- 描述:   civic_tooltip_spirit_of_rule_by_man_effects
- 需求:=>- civics:=>- NOR:=>- value:
- -  "自动化乌托邦"
- - civic_efficient_bureaucracy

- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - empire_size_penalty_mult:   0.25
- - planet_crime_mult:   0.25
- 随机权重:=>- 基础:   5
## <span title=civic_superhuman_economy style="border-bottom:1px dotted"> "超人经济"</span>
- 描述:   civic_tooltip_superhuman_economy_effects
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "精英主义"
- -  "权威主义"

- text:    "是一定程度的§Y%ethic_fanatic_authoritarian%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - leaders_cost_mult:   0.25
- - leaders_upkeep_mult:   0.25
- - councilor_skill_add:   3
- - planet_jobs_produces_mult:   -0.25
- 随机权重:=>- 基础:   0
## <span title=civic_idealistic_foundation style="border-bottom:1px dotted">civic_idealistic_foundation</span>
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   5
- - 拥有思潮:    "集体主义"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "宪政主义"
- -  "自由主义"

- text:    "是一定程度的§Y%ethic_fanatic_egalitarian%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - planet_stability_add:   10
- - pop_government_ethic_attraction:   0.15
- - pop_ethic_egalitarian_attraction_mult:   0.1
## <span title=civic_parental_authoritarianism style="border-bottom:1px dotted"> "父父子子"</span>
- 描述:    "—%MOD_PLANET_STABILITY_ADD%永远为§G100§!\n—%MOD_PLANET_AMENITIES_ADD%与%MOD_POP_HAPPINESS%永远为§Y0§!"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "精英主义"
- -  "权威主义"

- text:    "是一定程度的§Y%ethic_fanatic_authoritarian%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- hide_modifiers:   yes
- ai_weight:=>- 基础:   @ai_civic_default_base_weight
- 随机权重:=>- 基础:   @civic_default_random_weight
- 修正:=>- - planet_stability_add:   200
- - planet_amenities_mult:   -2
- - pop_happiness:   -2
## <span title=civic_void_hive style="border-bottom:1px dotted">civic_void_hive</span>
- ai_playable:=>- has_lithoids:   yes
- 描述:   civic_tooltip_void_hive_effects
- playable:=>- has_lithoids:   yes
- 前置条件:=>- 政体:=>- value:   auth_hive_mind
- ai_weight:=>- 基础:   @ai_civic_default_base_weight
- 随机权重:=>- 基础:   @civic_default_random_weight
- 修正:=>- - megastructure_build_speed_mult:   0.1
- - megastructures_cost_mult:   -0.1
- - councilor_gestalt_growth_exp_gain:   @gestalt_civic_node_xp_rate
## <span title=civic_machine_tactical_algorithms style="border-bottom:1px dotted">civic_machine_tactical_algorithms</span>
- modification:=>- add:=>- has_tradition:    "未来传统完成"
- has_technology:   tech_ascension_theory
- ai_playable:=>- has_machine_age_dlc:   yes
- playable:=>- has_machine_age_dlc:   yes
- 描述:   civic_machine_tactical_algorithms_effects
- 需求:=>- civics:=>- NOT:=>- value:   civic_machine_terminator
- 前置条件:=>- 政体:=>- value:   auth_machine_intelligence
- 修正:=>- - councilor_gestalt_legion_exp_gain:   @gestalt_civic_node_xp_rate
- - add_base_country_intel:   20
- swap_type:=>- 描述:   civic_machine_tactical_algorithms_effects
- trigger:=>- host_has_dlc:   Overlord
## <span title=civic_family_business style="border-bottom:1px dotted"> "§H§Y家族企业§!§!"</span>
- 随机权重:=>- 基础:   60
- 修正:=>- - 因子:   0
- - has_civic:   civic_empty_vagrant
- - NOR:=>- has_origin:   origin_ev_both_choosen
- has_civic:   civic_ev_planet_and_fleet
- has_ascension_perk:   ev_land_planets
- 描述:    "—£building£ §Y首都建筑§!会替换 £job_politician£ §Y%job_politician%§!岗位为 £job_executive£ §Y%job_executive_plural%§!\n—§Y奴隶§!人口额外产出§Y0.5§!£trade_value£ %TRADE_VALUE%\n—国家类型将被视为§Y%auth_corporate%§!\n—殖民星球后自动在新的殖民地开设§Y企业%BRANCH_OFFICES%§!"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "竞争主义"
- -  "个人主义"

- text:    "是一定程度的§Y%ethic_fanatic_capitalism%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - pop_demotion_time_mult:   1
- - planet_jobs_produces_mult:   0.1
- - branch_office_value_mult:   0.25
- - pop_ethic_capitalism_attraction_mult:   0.25
## <span title=civic_hive_upkeep_twister style="border-bottom:1px dotted">civic_hive_upkeep_twister</span>
- ai_playable:=>- host_has_dlc:   GalacticParagons
- playable:=>- host_has_dlc:   GalacticParagons
- 需求:=>- 前置条件:=>- 政体:=>- value:   auth_hive_mind
- 随机权重:=>- 基础:   4
- 修正:=>- - councilor_gestalt_regulatory_exp_gain:   @gestalt_civic_node_xp_rate
- - country_leader_cap_add:   1
- - leaders_upkeep_mult:   0.25
## <span title=civic_media_conglomerate style="border-bottom:1px dotted">civic_media_conglomerate</span>
- 需求:=>- 思潮:=>- NOR:=>- value:
- -  "单一主义"
- -  "排外主义"

- text:    "不接受任何程度的§Y排外主义§!"
- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- 修正:=>- - pop_citizen_happiness:   0.1
- - job_media_worker_add:   3
- - country_war_exhaustion_mult:   -0.1
- - planet_stability_add:   5
- 随机权重:=>- 基础:   25
- 修正:=>- - 因子:   1.5
- - 拥有思潮:    "崇外主义"
## <span title=civic_reeducated_labor style="border-bottom:1px dotted"> "奴役暴君"</span>
- 描述:    "—能够使用§Y%slavery_indentured%§!奴役方式\n—非§Y道德主义§!可以建造特殊建筑——§Y新竞技场§!，增加£job_gladiator£ §Y角斗士§!岗位，产出一定的£trade_value£ %TRADE_VALUE%并提高当地§Y陆军伤害§!\n—§Y市场经济§!下, 无经济危机时, 提供§Y+0.1§!%economic_situation_improve%和§Y-40§!%economic_crisis_threshold%。\n—§Y奴隶§!人口额外产出§Y0.75§!£trade_value£ %TRADE_VALUE%"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "权威主义"
- -  "个人主义"

- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 随机权重:=>- 基础:   25
- 修正:=>- - pop_cat_slave_political_power:   -0.25
- - slave_market_cost_mult:   -0.25
- - planet_jobs_slave_produces_mult:   0.25
- - pop_cat_slave_happiness:   -0.05
- leader_background_job_weight:=>- gladiator:   20
## <span title=civic_cyber_dictatorship style="border-bottom:1px dotted"> "§H§Y科研骑士§!§!"</span>
- 描述:    "—£building£ §Y首府建筑§!会替换部分£job_politician£ §Y%job_politician%§!岗位为£job_head_researcher£ §Y%job_head_researcher_plural%§!\n—£job_head_researcher£ %job_head_researcher_plural%不再产出研究点数，而提供£job_researcher£ %job_researcher_plural%岗位\n—£job_researcher£ %job_researcher_plural%额外提供£job_squire£ %job_squire_plural%岗位，但产出研究点数减半\n—£job_head_researcher£ %job_head_researcher_plural%将£job_squire£ %job_squire_plural%产出的£physics£ £society£ £engineering£ 研究点数转移到自己身上\n\n%MODIFIERS_TITLE%\n—%mod_country_scientist_cap_add%: §G+2§!\n—%mod_planet_building_research_lab_1_build_speed_mult%: §G+25%§!\n—研究花费: §R+25%§!\n—%mod_pop_ethic_materialist_attraction_mult%: §G+25%§!"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "技术主义"
- -  "机械主义"

- text:    "是一定程度的§Y%ethic_fanatic_materialist%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- hide_modifiers:   yes
- 随机权重:=>- 基础:   60
- 修正:=>- - 因子:   0
- - has_civic:   civic_empty_vagrant
- - NOR:=>- has_origin:   origin_ev_both_choosen
- has_civic:   civic_ev_planet_and_fleet
- has_ascension_perk:   ev_land_planets
- 修正:=>- - planet_building_research_lab_3_build_speed_mult:   0.25
- - planet_building_research_lab_1_build_speed_mult:   0.25
- - society_tech_cost_mult:   0.25
- - engineering_tech_cost_mult:   0.25
- - country_scientist_cap_add:   2
- - planet_building_mage_tower_1_build_speed_mult:   0.25
- - planet_building_research_lab_2_build_speed_mult:   0.25
- - planet_building_mage_tower_3_build_speed_mult:   0.25
- - planet_building_mage_tower_2_build_speed_mult:   0.25
- - physics_tech_cost_mult:   0.25
- - pop_ethic_materialist_attraction_mult:   0.25
## <span title=civic_conservative_armament style="border-bottom:1px dotted"> "帕拉贝卢姆"</span>
- 描述:   civic_tooltip_conservative_armament_effects
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "和平主义"
- -  "道德主义"

- text:    "是一定程度的§Y%ethic_fanatic_pacifist%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - country_naval_cap_mult:   0.15
- 随机权重:=>- 基础:   5
## <span title=civic_performance_appraisal style="border-bottom:1px dotted"> "绩效考核"</span>
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   5
- - 拥有思潮:    "自由主义"
- 需求:=>- 思潮:=>- NOR:=>- value:    "权威主义"
- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- 修正:=>- - species_leader_exp_gain:   0.15
- - councilor_skill_add:   1
- - trade_value_mult:   0.15
- - pop_cat_worker_political_power:   1
## <span title=civic_machine_unitary_cohesion style="border-bottom:1px dotted">civic_machine_unitary_cohesion</span>
- 随机权重:=>- 基础:   5
- 前置条件:=>- 政体:=>- value:   auth_machine_intelligence
- 修正:=>- - councilor_gestalt_regulatory_exp_gain:   @gestalt_civic_node_xp_rate
- - country_unity_produces_mult:   0.25
## <span title=civic_galactic_uterus style="border-bottom:1px dotted"> "银河子宫"</span>
- 描述:   civic_galactic_uterus_effects
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "竞争主义"
- -  "个人主义"

- text:    "是一定程度的§Y%ethic_fanatic_capitalism%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - pop_category_rulers_consumer_goods_upkeep_add:   0.5
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   5
- - 拥有思潮:    "个人主义"
## <span title=civic_divine_order style="border-bottom:1px dotted"> "种姓制度"</span>
- 随机权重:=>- 基础:   20
- 修正:=>- - 因子:   1.5
- - 拥有思潮:    "权威主义"
- 描述:   "可以建造 £building£ §Y%building_noble_estates%§!建筑添加额外的 £job_noble£ §Y%job_noble%§!岗位\n—§Y奴隶§!人口额外产出§Y0.5§!£trade_value£ %TRADE_VALUE%\n—§Y市场经济§!下, 无经济危机时, 提供§Y+0.1§!%economic_situation_improve%和§Y-40§!%economic_crisis_threshold%。"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "精神主义"
- -  "教权主义"

- text:    "是一定程度的§Y%ethic_fanatic_spiritualist%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - country_leader_pool_size:   -1
- - planet_stability_add:   10
- - pop_demotion_time_mult:   1.5
- - planet_jobs_worker_produces_mult:   0.1
- - planet_jobs_specialist_produces_mult:   0.05
- - pop_cat_ruler_happiness:   0.05
- - planet_jobs_slave_produces_mult:   0.15
- - num_tech_alternatives_add:   -1
## <span title=civic_heart_of_the_unity style="border-bottom:1px dotted"> "和谐集体"</span>
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   5
- - 拥有思潮:    "教权主义"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "精神主义"
- -  "教权主义"
- -  "和平主义"
- -  "道德主义"

- text:    "一定程度上偏向§Y%ethic_fanatic_spiritualist%§!或者§Y%ethic_fanatic_pacifist%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - empire_size_pops_mult:   -0.15
- - country_unity_produces_mult:   0.05
- - planet_crime_mult:   -0.2
- - pop_ethic_socialism_attraction_mult:   0.15
## <span title=civic_coalition_government style="border-bottom:1px dotted"> "§H§Y主权邦联§!§!"</span>
- 随机权重:=>- 基础:   50
- 修正:=>- - 因子:   0
- - has_civic:   civic_empty_vagrant
- - NOR:=>- has_origin:   origin_ev_both_choosen
- has_civic:   civic_ev_planet_and_fleet
- has_ascension_perk:   ev_land_planets
- 描述:    "—£building£ §Y首府建筑§!会替换部分 £job_politician£ §Y%job_politician%§!岗位为 £job_sovereign_representative£ §Y%job_sovereign_representative_plural%§!岗位\n—每个£job_sovereign_representative£ §Y%job_sovereign_representative_plural%§!岗位额外§G+1%§!%MOD_DIPLO_WEIGHT_MULT%\n—被雇佣的§Y领袖§!不再需要花费£unity£ 凝聚力来维护，但你也无法再解雇他们\n—§Y解锁舰船类型：§!私人殖民船\n—你的§Y附属国§!不能签订含有以下条款的协议：\n——%t%%TRIGGER_FAIL%§Y%subject_cannot_expand%§!\n——%t%%TRIGGER_FAIL%§Y允许宗主国不加入附属国战争§!\n——%t%%TRIGGER_FAIL%§Y%subject_can_not_do_diplomacy%§!"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "多元主义"
- -  "崇外主义"

- text:    "是一定程度的§Y%ethic_fanatic_xenophile%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - diplomacy_upkeep_mult:   -0.15
- - local_trade_protection_add:   -10
- - divided_patrongage_max_subjects:   3
- - pop_ethic_xenophile_attraction_mult:   0.25
## <span title=civic_characteristic_socialism_pioneer style="border-bottom:1px dotted"> "%civic_characteristic_socialism%"</span>
- leader_background_job_weight:=>- merchant:   200
- "grassroot_cadre":   0
- "labour_hero":   0
- mogul:   200
- trader:   100
- 描述:    "—开始游戏时解锁%reform_and_opening_up%政策。\n—针对新时代的新形势，我们要§E转换新思想§!，§Y提出新要求§!，§R拿出新方法§!，§B打开新局面§!，§M走向新征程§!。"
- 需求:=>- civics:=>- OR:=>- value:
- -  "§H§Y思想设计师§!§!"
- -  "§H§Y民族与阶级§!§!"
- -  "§H§Y工人贵族§!§!"

- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- hide_modifiers:   yes
- icon:   gfx/interface/icons/governments/civics/civic_characteristic_socialism.dds
- 随机权重:=>- 基础:   5
- 修正:=>- - 因子:   10
- - has_civic:    "§H§Y工人贵族§!§!"
- 修正:=>- - job_core_party_members_per_pop:   0.02
- - job_merchant_per_pop:   0.02
- - planet_emigration_push_mult:   0.5
- - planet_jobs_slave_produces_mult:   0.1
- - country_pop_enslaved_mult:   0.15
- alternate_civic_version:    "特色社会主义"
## <span title=civic_barbaric_despoilers style="border-bottom:1px dotted"> "§H§Y野蛮掠夺者§!§!"</span>
- 描述:    "—£building£ §Y首都建筑§!将所有的£job_politician£ §Y%job_politician%§!岗位和 £job_enforcer£ §Y%job_enforcer_plural%§!岗位替换为£job_criminal£ §Y%job_criminal_plural%§!岗位和 £job_soldier£ §Y%job_mercenary_plural%§!岗位\n—§R无法建造§Y%building_precinct_house%§!§!，£job_criminal£ %job_criminal_plural%将额外提供£mod_country_admin_cap_add£ %MOD_COUNTRY_ADMIN_CAP_ADD%\n—不能成立（但可以加入）除§Y军事同盟§!和§Y霸权联盟§!以外的§Y联邦§!\n—对其它所有帝国拥有§Y“%casus_belli_cb_despoliation%”§!宣战理由\n—%allow_raiding%\n—降低大部分其他帝国对你的§Y评价§!"
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "干涉主义"
- -  "军国主义"

- text:    "是一定程度的§Y%ethic_fanatic_militarist%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - local_trade_protection_add:   -10
- - pop_cat_criminal_happiness:   0.15
- - pop_cat_criminal_political_power:   4
- - pop_ethic_militarist_attraction_mult:   0.25
- 随机权重:=>- 基础:   60
- 修正:=>- - 因子:   0
- - has_civic:   civic_empty_vagrant
- - NOR:=>- has_origin:   origin_ev_both_choosen
- has_civic:   civic_ev_planet_and_fleet
- has_ascension_perk:   ev_land_planets
## <span title=civic_globalism style="border-bottom:1px dotted"> "全球主义"</span>
- 随机权重:=>- 基础:   15
- 描述:    "—通过§Y增强投标§!，他们的星球有更高的几率被提名主持§Y银河市场§!，使用§Y增强提名投标§!花费更少的影响力\n—§Y商业协议§!不需要花费影响力维持\n—提高§Y贸易联盟§!飞地的评价\n—§Y企业家派系§!对§Y贸易联邦§!提供额外支持"
- 需求:=>- 思潮:=>- value:    "崇外主义"
- OR:=>- value:
- -  "竞争主义"
- -  "个人主义"

- text:    "是一定程度的§Y%ethic_fanatic_capitalism%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - country_trade_fee:   -0.05
- - country_trade_attractiveness:   0.33
- - DIPLO_WEIGHT_ECONOMY_MULT:   0.2
## <span title=civic_crusader_spirit_corporate style="border-bottom:1px dotted">civic_crusader_spirit_corporate</span>
- ai_playable:=>- host_has_dlc:   GalacticParagons
- 描述:   civic_tooltip_crusader_spirit_corporate_effects
- playable:=>- host_has_dlc:   GalacticParagons
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "干涉主义"
- -  "军国主义"

- text:    "是一定程度的§Y%ethic_fanatic_militarist%§!"
- 前置条件:=>- OR:=>- 政体:=>- value:   auth_corporate
- 随机权重:=>- 基础:   4
- 修正:=>- - local_trade_protection_add:   20
- - ships_upkeep_mult:   -0.1
- swap_type:=>- trigger:=>- host_has_dlc:   Overlord
## <span title=civic_individual_machine_predictive_analysis style="border-bottom:1px dotted">civic_individual_machine_predictive_analysis</span>
- ai_weight:=>- 基础:   @ai_civic_default_base_weight
- 随机权重:=>- 基础:   @civic_default_random_weight
- 需求:=>- 思潮:=>- OR:=>- value:
- -  "技术主义"
- -  "机械主义"

- text:    "是一定程度的§Y%ethic_fanatic_materialist%§!"
- 前置条件:=>- 思潮:=>- NOT:=>- value:    "完形意识"
- 修正:=>- - scientist_exp_gain:   0.15
- - num_tech_alternatives_add:   2
- - intel_decryption_add:   1
