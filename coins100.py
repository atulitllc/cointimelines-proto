# Coins 51 to 100. Thinner histories; events kept to well documented dates. Supply comes from CoinGecko (see build).
from coins50 import W, E
D = {}
def coin(key, cgid, slug, name, sym, cats, color, color2, label, founders, consensus, origin, primary, wiki, events=()):
    D[key] = dict(cgid=cgid, slug=slug, name=name, sym=sym, cats=cats, color=color, color2=color2, founded=None, founded_label=label,
        founders=founders, origin=origin, facts=[("Launched", label), ("Consensus or platform", consensus)], primary=primary + [W(wiki)], wiki=wiki, events=list(events))
coin("tao","bittensor","bittensor","Bittensor","TAO",["AI and compute","Layer 1"],"#000000","#555555","2021","Jacob Steeves and Ala Shaabana; Opentensor Foundation","Own chain built with Substrate; validators score AI work in subnets",
 ["Bittensor is a network where machine learning models compete in subnets and earn TAO for useful work, as judged by validators. It was started by Jacob Steeves and Ala Shaabana through the Opentensor Foundation.","Like Bitcoin, TAO has a fixed maximum of 21 million coins and a halving style issuance schedule."],
 [("Bittensor docs","https://docs.bittensor.com/")],"Bittensor")
coin("qnt","quant-network","quant","Quant","QNT",["Interoperability"],"#000000","#5E5E5E","2018","Gilbert Verdian","ERC-20 token for the Overledger interoperability platform",
 ["Quant was founded in the UK by Gilbert Verdian, who previously worked on security and payments for governments and banks. Its Overledger software aims to connect enterprise systems with many blockchains.","QNT is an ERC-20 token sold in 2018 and used to pay for licenses on the platform."],
 [("Quant official site","https://quant.network/")],"Quant (company)")
coin("okb","okb","okb","OKB","OKB",["Exchange token"],"#000000","#3075EE","2018","OKX (formerly OKEx), founded by Star Xu","Exchange token; also gas on OKX's X Layer network",
 ["OKB is the utility token of OKX, one of the largest crypto exchanges, founded by Star Xu. Holders get trading fee discounts and access to token sales on the exchange.","OKX has burned large amounts of OKB over time to reduce its supply."],
 [("OKX: about OKB","https://www.okx.com/okb")],"OKX")
coin("pepe","pepe","pepe","Pepe","PEPE",["Meme"],"#3D8130","#6CC24A","Apr 2023","Anonymous team; based on the Pepe the Frog character by artist Matt Furie, who is not involved","ERC-20 token on Ethereum",
 ["Pepe is a meme coin launched on Ethereum in April 2023 by an anonymous team, themed on the Pepe the Frog cartoon created by Matt Furie. It has no stated utility; its own site calls it a meme coin with no intrinsic value.","It rose very fast in its first weeks and became one of the largest meme coins."],
 [("Pepe official site","https://www.pepe.vip/"),("PEPE token on Etherscan","https://etherscan.io/token/0x6982508145454ce325ddbe47a25d4ec3d2311933")],"Pepe (cryptocurrency)")
coin("bgb","bitget-token","bitget-token","Bitget Token","BGB",["Exchange token"],"#00F0FF","#1DA2B4","2021","Bitget exchange","Exchange token on Ethereum",
 ["BGB is the exchange token of Bitget, a crypto exchange known for derivatives and copy trading. It gives holders fee discounts and access to token launches on the platform."],
 [("Bitget: BGB","https://www.bitget.com/bgb")],"Bitget")
coin("kcs","kucoin-shares","kucoin-token","KuCoin Token","KCS",["Exchange token"],"#24AE8F","#1BA27A","2017","KuCoin exchange, co founded by Michael Gan and Johnny Lyu","Exchange token; native to KuCoin Community Chain",
 ["KCS is the token of the KuCoin exchange, launched in 2017. KuCoin shares part of its trading fee revenue with KCS holders and has run regular buybacks and burns."],
 [("KuCoin: KCS","https://www.kucoin.com/kcs")],"KuCoin")
coin("gt","gatechain-token","gatetoken","GateToken","GT",["Exchange token"],"#2354E6","#17E6A1","2019","Gate.io exchange, founded by Lin Han","Exchange token; native to GateChain",
 ["GT is the token of the Gate.io exchange and its GateChain network. It is used for fee discounts and gas on GateChain, and the exchange has burned tokens over time."],
 [("Gate: GT","https://www.gate.io/gt")],"Gate.io")
coin("aero","aerodrome-finance","aerodrome","Aerodrome","AERO",["DeFi"],"#0433FF","#5B7CFF","Aug 2023","Built by the team behind Velodrome on Optimism","Token on Base (Coinbase's layer 2)",
 ["Aerodrome is the largest decentralized exchange on Base, the Ethereum layer 2 network launched by Coinbase. It is a fork of Velodrome and uses a vote escrow model where locked AERO holders direct token rewards to pools."],
 [("Aerodrome docs","https://aerodrome.finance/docs")],"Base (blockchain)")
coin("nexo","nexo","nexo","Nexo","NEXO",["Exchange token","DeFi"],"#1A4199","#4DA3FF","2018","Antoni Trenchev and Kosta Kantchev","Token on Ethereum",
 ["Nexo is a crypto lending company founded in 2018 by Antoni Trenchev and Kosta Kantchev, with roots in the Bulgarian fintech Credissimo. The NEXO token gives holders better rates on the platform.","In January 2023 Nexo agreed to pay 45 million dollars to settle SEC and state charges over its Earn Interest Product."],
 [("SEC press release 2023-14","https://www.sec.gov/newsroom/press-releases/2023-14")],"Nexo")
coin("zro","layerzero","layerzero","LayerZero","ZRO",["Interoperability"],"#000000","#6B6B6B","Jun 20, 2024","Bryan Pellegrino, Ryan Zarick and Caleb Banister of LayerZero Labs","Token for a cross chain messaging protocol",
 ["LayerZero is a messaging protocol that lets apps send data and tokens between blockchains. It was founded by Bryan Pellegrino, Ryan Zarick and Caleb Banister.","The ZRO token launched on June 20, 2024 with an airdrop to users."],
 [("LayerZero docs","https://docs.layerzero.network/")],"LayerZero",
 [E("2024-06-20","launch","ZRO token launch","LayerZero airdrops its ZRO token.",["ZRO launched on June 20, 2024. LayerZero asked airdrop claimants to make a small donation per token, an unusual condition that drew debate."],[("LayerZero docs","https://docs.layerzero.network/")])])
coin("cake","pancakeswap-token","pancakeswap","PancakeSwap","CAKE",["DeFi"],"#1FC7D4","#7645D9","Sep 2020","Anonymous team","Token on BNB Smart Chain",
 ["PancakeSwap is the largest decentralized exchange on BNB Smart Chain, launched in September 2020 by an anonymous team. It copied the automated market maker design of Uniswap and SushiSwap and added farms, lotteries and NFTs, all with a bakery theme."],
 [("PancakeSwap docs","https://docs.pancakeswap.finance/")],"PancakeSwap")
coin("xdc","xdce-crowd-sale","xdc-network","XDC Network","XDC",["Layer 1","Payments"],"#1E3A8A","#3B82F6","2019","Ritesh Kakkad and Atul Khekade","Delegated proof of stake (XinFin XDPoS)",
 ["XDC Network, developed by XinFin, is an Ethereum compatible chain aimed at trade finance and enterprise payments. It was co founded by Ritesh Kakkad and Atul Khekade and launched its mainnet in 2019."],
 [("XDC docs","https://docs.xdc.network/")],"XDC Network")
coin("pyth","pyth-network","pyth","Pyth Network","PYTH",["Oracle","DeFi"],"#7142CF","#E6DAFE","Nov 20, 2023","Started with Jump Crypto and a group of trading firms; governed by the Pyth DAO","Oracle network token on Solana",
 ["Pyth is an oracle network that publishes price data supplied directly by exchanges and trading firms. It began on Solana in 2021 and now serves many chains.","The PYTH token launched with an airdrop on November 20, 2023."],
 [("Pyth docs","https://docs.pyth.network/")],"Pyth Network",
 [E("2023-11-20","launch","PYTH airdrop","Pyth launches its governance token.",["PYTH launched on November 20, 2023 with an airdrop to apps and users that had relied on Pyth data."],[("Pyth docs","https://docs.pyth.network/")])])
coin("ethfi","ether-fi","ether-fi","ether.fi","ETHFI",["DeFi"],"#2D2B55","#8A7DFF","Mar 2024","Mike Silagadze","Governance token on Ethereum",
 ["ether.fi is a liquid restaking protocol founded by Mike Silagadze. Users deposit ETH and receive eETH, which earns staking and restaking rewards while staying tradable. ETHFI is its governance token, launched in March 2024."],
 [("ether.fi docs","https://etherfi.gitbook.io/etherfi")],"EigenLayer")
coin("strk","starknet","starknet","Starknet","STRK",["Layer 2"],"#0C0C4F","#EC796B","Feb 20, 2024","Eli Ben-Sasson, Uri Kolodny, Alessandro Chiesa and Michael Riabzev of StarkWare","Validity rollup (ZK rollup) on Ethereum",
 ["Starknet is an Ethereum layer 2 network built by StarkWare, whose founders include Eli Ben-Sasson, a co inventor of STARK proofs. It batches transactions and proves them to Ethereum with zero knowledge proofs.","The STRK token was airdropped on February 20, 2024."],
 [("Starknet docs","https://docs.starknet.io/"),("Voyager explorer","https://voyager.online/")],"StarkWare Industries",
 [E("2024-02-20","launch","STRK airdrop","Starknet distributes its STRK token.",["STRK became claimable on February 20, 2024. Eligibility rules that left out many smaller users caused controversy."],[("Starknet docs","https://docs.starknet.io/")])])
coin("flr","flare-networks","flare","Flare","FLR",["Layer 1","Oracle"],"#E62058","#FF7A9C","Jan 9, 2023","Hugo Philion and Sean Rowan","Avalanche style consensus with built in data protocols",
 ["Flare is an Ethereum compatible layer 1 founded by Hugo Philion and Sean Rowan, with built in oracle and cross chain data protocols. FLR was first promised to XRP holders in a December 2020 snapshot.","After long delays, the FLR token distribution began on January 9, 2023."],
 [("Flare docs","https://dev.flare.network/")],"Flare Network",
 [E("2023-01-09","launch","FLR token distribution","Flare begins distributing FLR to eligible XRP holders.",["Distribution of FLR started on January 9, 2023, more than two years after the December 2020 XRP snapshot."],[("Flare docs","https://dev.flare.network/")])])
coin("tia","celestia","celestia","Celestia","TIA",["Layer 1","Modular"],"#7B2BF9","#B57BFF","Oct 31, 2023","Mustafa Al-Bassam, Ismail Khoffi and John Adler","Proof of stake (Cosmos SDK); data availability layer",
 ["Celestia is a modular blockchain that focuses on data availability: it orders and publishes data for other chains and rollups rather than running smart contracts itself. Co founder Mustafa Al-Bassam wrote the LazyLedger paper it is based on.","Celestia's mainnet launched on October 31, 2023 with a TIA airdrop."],
 [("Celestia docs","https://docs.celestia.org/"),("LazyLedger paper (arXiv)","https://arxiv.org/abs/1905.09274")],"Celestia (blockchain)",
 [E("2023-10-31","launch","Celestia mainnet beta","Celestia launches and TIA starts trading.",["Celestia's mainnet beta went live on October 31, 2023."],[("Celestia docs","https://docs.celestia.org/")])])
coin("trump","official-trump","official-trump","Official Trump","TRUMP",["Meme"],"#C8102E","#F2C14E","Jan 17, 2025","Launched by Fight Fight Fight LLC and CIC Digital, companies tied to Donald Trump","Token on Solana",
 ["Official Trump is a meme coin launched on Solana on January 17, 2025, three days before Donald Trump's inauguration, and promoted by Trump himself. Its website says it is not an investment. Most of the supply was held by Trump affiliated companies under a vesting schedule."],
 [("Official Trump site","https://gettrumpmemes.com/")],"$Trump",
 [E("2025-01-17","launch","TRUMP meme coin launches","Donald Trump announces his own meme coin.",["The TRUMP token launched on January 17, 2025 and reached a multi billion dollar valuation within days."],[W("$Trump")])])
coin("ray","raydium","raydium","Raydium","RAY",["DeFi"],"#2B6AFF","#C200FB","Feb 2021","Anonymous team","Token on Solana",
 ["Raydium is an automated market maker on Solana launched in early 2021. It became a main venue for new Solana tokens, including many meme coins that start on Pump.fun and later trade on Raydium pools."],
 [("Raydium docs","https://docs.raydium.io/")],"Solana (blockchain platform)")
coin("crv","curve-dao-token","curve","Curve DAO","CRV",["DeFi"],"#40649F","#FF0000","Aug 2020","Michael Egorov","Governance token on Ethereum",
 ["Curve Finance, founded by physicist Michael Egorov, is a decentralized exchange designed for swapping similar assets like stablecoins with low slippage. Its CRV token, launched in August 2020, introduced the vote escrow model many protocols later copied.","Curve also issues its own stablecoin, crvUSD."],
 [("Curve docs","https://docs.curve.finance/")],"Curve Finance")
coin("fet","fetch-ai","artificial-superintelligence-alliance","Artificial Superintelligence Alliance","FET",["AI and compute"],"#1D2951","#3A7BD5","2019 (as Fetch.ai)","Humayun Sheikh, Toby Simpson and Thomas Hain (Fetch.ai)","Token on Ethereum and Fetch.ai's Cosmos based chain",
 ["FET began as the token of Fetch.ai, a UK company founded by Humayun Sheikh, an early investor in DeepMind. Fetch.ai builds tools for autonomous AI agents.","In 2024 Fetch.ai, SingularityNET and Ocean Protocol merged their tokens into the Artificial Superintelligence Alliance, with FET as the combined token."],
 [("Fetch.ai docs","https://fetch.ai/docs")],"Fetch.ai")
coin("ldo","lido-dao","lido","Lido DAO","LDO",["DeFi"],"#F69988","#00A3FF","Dec 2020","Lido DAO, with founding contributors including Konstantin Lomashuk and Vasiliy Shapovalov","Governance token on Ethereum",
 ["Lido is the largest liquid staking protocol for Ethereum. Users stake ETH and receive stETH, a token that earns staking rewards and can still be traded. LDO governs the Lido DAO, which launched in December 2020 when Ethereum's Beacon Chain went live."],
 [("Lido docs","https://docs.lido.fi/")],"Lido Finance")
coin("xtz","tezos","tezos","Tezos","XTZ",["Layer 1"],"#2C7DF7","#0F62FE","Jun 30, 2018","Arthur and Kathleen Breitman","Liquid proof of stake",
 ["Tezos was designed by Arthur Breitman and Kathleen Breitman, with a 2014 whitepaper describing a blockchain that can upgrade itself through on chain voting. Its July 2017 fundraiser raised about 232 million dollars, then a record.","A dispute between the founders and the Tezos Foundation's first president delayed launch and led to class action suits. The network went live on June 30, 2018."],
 [("Tezos docs","https://docs.tezos.com/"),("TzKT explorer","https://tzkt.io/")],"Tezos",
 [E("2018-06-30","launch","Tezos betanet launches","Tezos goes live after a year of delays.",["Tezos launched its betanet on June 30, 2018, almost a year after its fundraiser."],[W("Tezos"),("Tezos docs","https://docs.tezos.com/")])])
coin("op","optimism","optimism","Optimism","OP",["Layer 2"],"#FF0420","#FF5A6E","May 31, 2022","Jinglan Wang, Karl Floersch, Kevin Ho and Ben Jones","Optimistic rollup on Ethereum (OP Stack)",
 ["Optimism is an Ethereum layer 2 network built by OP Labs and governed by the Optimism Collective. Its open source OP Stack also powers other chains, including Coinbase's Base.","The OP token launched with an airdrop on May 31, 2022."],
 [("Optimism docs","https://docs.optimism.io/"),("Optimistic Etherscan","https://optimistic.etherscan.io/")],"Optimism (blockchain)",
 [E("2022-05-31","launch","OP airdrop","Optimism launches the OP governance token.",["The OP token airdrop began on May 31, 2022. Heavy demand caused problems with the network's public infrastructure on the first day."],[("Optimism docs","https://docs.optimism.io/")])])
coin("gno","gnosis","gnosis","Gnosis","GNO",["Layer 1"],"#133629","#3E6957","Apr 2017","Martin Koppelmann and Stefan George","Proof of stake (Gnosis Chain)",
 ["Gnosis started in 2015 as a prediction market project inside ConsenSys, founded by Martin Koppelmann and Stefan George. Its April 2017 token sale raised about 12.5 million dollars in minutes.","Gnosis later built the Safe multisig wallet, which became its own company, and Gnosis Chain, an Ethereum compatible chain secured by GNO staking."],
 [("Gnosis docs","https://docs.gnosischain.com/")],"Gnosis (company)")
coin("cfx","conflux-token","conflux","Conflux","CFX",["Layer 1"],"#1A1A1A","#4A90E2","Oct 2020","Fan Long and Ming Wu","Hybrid proof of work and proof of stake (Tree Graph)",
 ["Conflux is a public blockchain based in China, co founded by Fan Long, with research ties to Andrew Yao at Tsinghua University. It uses a Tree Graph structure so blocks can be processed in parallel. Its mainnet, called Tethys, launched in October 2020."],
 [("Conflux docs","https://doc.confluxnetwork.org/")],"Conflux Network")
coin("dcr","decred","decred","Decred","DCR",["Layer 1"],"#2ED6A1","#2970FF","Feb 8, 2016","Developers from Company 0, including Jake Yocom-Piatt","Hybrid proof of work and proof of stake",
 ["Decred was launched on February 8, 2016 by developers who had worked on btcd, a Bitcoin node written in Go. It combines proof of work mining with proof of stake voting, so ticket holders approve blocks and vote on changes to the rules.","Decred also has a treasury funded by part of each block reward and governed by stakeholders."],
 [("Decred docs","https://docs.decred.org/"),("Decred block explorer","https://dcrdata.decred.org/")],"Decred",
 [E("2016-02-08","launch","Decred launches","Decred's mainnet starts.",["Decred launched on February 8, 2016 with a small airdrop and a premine for its developers."],[W("Decred"),("Decred docs","https://docs.decred.org/")])])
coin("grt","the-graph","the-graph","The Graph","GRT",["Infrastructure"],"#6747ED","#A48CFF","Dec 17, 2020","Yaniv Tal, Brandon Ramirez and Jannis Pohlmann","Token on Ethereum and Arbitrum for an indexing network",
 ["The Graph is an indexing network that organizes blockchain data so apps can query it quickly through subgraphs. It was founded by Yaniv Tal, Brandon Ramirez and Jannis Pohlmann.","Its mainnet and the GRT token launched on December 17, 2020."],
 [("The Graph docs","https://thegraph.com/docs/")],"The Graph",
 [E("2020-12-17","launch","The Graph mainnet","The Graph network and GRT launch.",["The Graph's decentralized network launched on December 17, 2020 and GRT began trading on major exchanges."],[("The Graph docs","https://thegraph.com/docs/")])])
coin("bonk","bonk","bonk","Bonk","BONK",["Meme"],"#F8A11F","#FF5C01","Dec 25, 2022","Anonymous community contributors","Token on Solana",
 ["Bonk is a dog themed meme coin on Solana. It was airdropped to Solana users on December 25, 2022, a few weeks after the FTX collapse had crushed the Solana ecosystem, and helped revive interest in the chain."],
 [("Bonk official site","https://bonkcoin.com/")],"Bonk (cryptocurrency)",
 [E("2022-12-25","launch","BONK Christmas airdrop","Half of BONK's supply is airdropped to the Solana community.",["Bonk launched on December 25, 2022 with about half of its supply given away to Solana users, NFT holders and developers."],[("Bonk official site","https://bonkcoin.com/")])])
coin("jto","jito-governance-token","jito","Jito","JTO",["DeFi"],"#1D1D1D","#71D88E","Dec 7, 2023","Lucas Bruder and Zano Sherwani of Jito Labs","Token on Solana",
 ["Jito runs a liquid staking pool and MEV infrastructure for Solana, founded by Lucas Bruder and Zano Sherwani. JitoSOL lets users stake SOL while keeping a tradable token.","The JTO governance token was airdropped on December 7, 2023, one of the events that brought new attention to Solana."],
 [("Jito docs","https://www.jito.network/docs/")],"Solana (blockchain platform)",
 [E("2023-12-07","launch","JTO airdrop","Jito launches the JTO token.",["JTO launched on December 7, 2023, and many recipients received several thousand dollars worth of tokens."],[("Jito docs","https://www.jito.network/docs/")])])
coin("lunc","terra-luna","terra-luna-classic","Terra Luna Classic","LUNC",["Layer 1"],"#172852","#FFD83D","2019 (as LUNA)","Do Kwon and Daniel Shin of Terraform Labs","Proof of stake (Cosmos SDK)",
 ["LUNC is the original Terra chain's token, first called LUNA. Terraform Labs, founded by Do Kwon and Daniel Shin, used it to back UST, an algorithmic stablecoin.","In May 2022 UST lost its dollar peg, and the mint and burn mechanism printed trillions of LUNA, wiping out about 40 billion dollars in value. A new chain took the LUNA name, and the original became Terra Classic (LUNC). Do Kwon later pleaded guilty to fraud in the US."],
 [("SEC press release on Terraform settlement","https://www.sec.gov/newsroom/press-releases/2024-73")],"Terra (blockchain)",
 [E("2022-05-09","crash","UST loses its peg","Terra's stablecoin collapses, taking LUNA with it.",["UST slipped below one dollar on May 9, 2022 and kept falling. Within days LUNA's supply exploded and its price fell by more than 99.9 percent. Our LUNC price data starts later."],[W("Terra (blockchain)"),("SEC press release on Terraform settlement","https://www.sec.gov/newsroom/press-releases/2024-73")])])
coin("bat","basic-attention-token","basic-attention-token","Basic Attention Token","BAT",["Advertising"],"#FF5000","#9E1F63","May 31, 2017","Brendan Eich and Brian Bondy","Token on Ethereum",
 ["BAT is the token behind the Brave browser's privacy friendly ads. Brave was founded by Brendan Eich, creator of JavaScript and co founder of Mozilla, and Brian Bondy. Users who opt in to Brave ads can earn BAT.","The BAT token sale on May 31, 2017 raised about 35 million dollars in under a minute."],
 [("Basic Attention Token whitepaper","https://basicattentiontoken.org/static-assets/documents/BasicAttentionTokenWhitePaper-4.pdf")],"Brave (web browser)",
 [E("2017-05-31","launch","BAT token sale","Brave raises about 35 million dollars in seconds.",["The BAT sale on May 31, 2017 sold out in about 30 seconds, an example of the ICO frenzy that year."],[W("Brave (web browser)")])])
coin("ar","arweave","arweave","Arweave","AR",["Storage"],"#222326","#7B7B7B","Jun 2018","Sam Williams and William Jones","Proof of access mining (SPoRA)",
 ["Arweave is a storage network for permanent data, started by Sam Williams and William Jones in the UK. Users pay once to store data that miners are rewarded to keep forever, funded by an endowment. Its mainnet launched in June 2018."],
 [("Arweave docs","https://docs.arweave.org/")],"Arweave")
coin("ens","ethereum-name-service","ethereum-name-service","Ethereum Name Service","ENS",["Infrastructure"],"#5298FF","#5A9DED","Nov 8, 2021","Nick Johnson","Governance token on Ethereum",
 ["Ethereum Name Service maps readable names like alice.eth to wallet addresses and other records. It was created by Nick Johnson, then at the Ethereum Foundation, and launched in 2017.","The ENS governance token was airdropped to .eth name holders on November 8, 2021."],
 [("ENS docs","https://docs.ens.domains/")],"Ethereum Name Service",
 [E("2021-11-08","launch","ENS airdrop","ENS gives governance tokens to name holders.",["ENS launched its token and DAO on November 8, 2021, airdropping ENS to past and current .eth holders."],[("ENS docs","https://docs.ens.domains/")])])
coin("floki","floki","floki","Floki","FLOKI",["Meme"],"#F3BA2F","#E6A100","Jun 2021","Anonymous community team","Token on Ethereum and BNB Smart Chain",
 ["Floki is a meme coin named after Elon Musk's Shiba Inu dog, launched in mid 2021. Its team spent heavily on marketing, including ads on London buses that drew a warning from UK regulators."],
 [("Floki official site","https://floki.com/")],"Floki (cryptocurrency)")
coin("eigen","eigenlayer","eigenlayer","EigenLayer","EIGEN",["DeFi","Infrastructure"],"#1A0C6D","#7D6DF0","Oct 1, 2024","Sreeram Kannan","Token on Ethereum",
 ["EigenLayer is a restaking protocol founded by Sreeram Kannan, a former University of Washington professor. It lets staked ETH secure other services in exchange for extra rewards and slashing risk.","EIGEN became transferable on October 1, 2024."],
 [("EigenLayer docs","https://docs.eigenlayer.xyz/")],"EigenLayer")
coin("comp","compound-governance-token","compound","Compound","COMP",["DeFi"],"#00D395","#070A0E","Jun 15, 2020","Robert Leshner and Geoffrey Hayes","Governance token on Ethereum",
 ["Compound is a lending protocol on Ethereum founded by Robert Leshner and Geoffrey Hayes in 2017. When it began handing out the COMP governance token to users on June 15, 2020, it kicked off yield farming and the DeFi summer of 2020."],
 [("Compound docs","https://docs.compound.finance/")],"Compound (company)",
 [E("2020-06-15","launch","COMP distribution begins","Liquidity mining starts DeFi summer.",["Compound began distributing COMP to borrowers and lenders on June 15, 2020. Copycat programs spread across DeFi within weeks."],[("Compound docs","https://docs.compound.finance/")])])
coin("iota","iota","iota","IOTA","IOTA",["Layer 1","Internet of things"],"#131F37","#00E0CA","2016","David Sonstebo, Sergey Ivancheglo, Dominik Schiener and Serguei Popov","Originally the Tangle, a directed acyclic graph; later delegated proof of stake",
 ["IOTA was founded in 2015 by David Sonstebo, Sergey Ivancheglo, Dominik Schiener and Serguei Popov, aiming at machine to machine payments for the internet of things. It started with the Tangle, a structure without blocks or fees.","The IOTA Foundation, a nonprofit in Berlin, oversees development."],
 [("IOTA docs","https://docs.iota.org/")],"IOTA (technology)")
coin("s","sonic-3","sonic","Sonic (formerly Fantom)","S",["Layer 1"],"#1969FF","#13B5EC","Dec 2024 (Fantom since 2019)","Ahn Byung Ik founded Fantom; Andre Cronje became a key developer","Proof of stake (Lachesis based)",
 ["Sonic is the successor to Fantom, a fast, Ethereum compatible layer 1 founded in 2018 by South Korean computer scientist Ahn Byung Ik. DeFi developer Andre Cronje became its best known builder.","In late 2024 Fantom relaunched as Sonic with a new chain and the S token, with FTM convertible one to one."],
 [("Sonic docs","https://docs.soniclabs.com/")],"Fantom (blockchain)")
coin("rune","thorchain","thorchain","THORChain","RUNE",["DeFi","Layer 1"],"#00CCFF","#33FF99","2018","A pseudonymous team; John-Paul Thorbjornsen is a known contributor","Proof of stake (Cosmos SDK)",
 ["THORChain is a chain that lets users swap native coins across blockchains, such as real BTC for real ETH, without wrapped tokens. It was built by a mostly pseudonymous team and uses RUNE as the asset paired in every pool.","Its multi chain mainnet launched in 2021, and it suffered several costly exploits that year."],
 [("THORChain docs","https://docs.thorchain.org/")],"THORChain")
coin("wif","dogwifcoin","dogwifhat","dogwifhat","WIF",["Meme"],"#C69C6D","#8C5A3C","Nov 2023","Anonymous","Token on Solana",
 ["dogwifhat is a Solana meme coin based on a photo of a Shiba Inu wearing a pink knitted hat. It launched in late 2023 and became one of the largest meme coins in 2024, when fans crowdfunded to put the dog on the Las Vegas Sphere."],
 [("dogwifhat token on Solscan","https://solscan.io/token/EKpQGSJtjMFqKZ9KQanSqYXRcF8fBopzLHYxdM65zcjm")],"Dogwifhat")
coin("akt","akash-network","akash","Akash Network","AKT",["AI and compute"],"#FF414C","#C1232B","Sep 2020","Greg Osuri and Adam Bozanich","Proof of stake (Cosmos SDK)",
 ["Akash Network is a marketplace for cloud computing, where people rent out spare servers and GPUs. It was founded by Greg Osuri and Adam Bozanich and launched its mainnet in September 2020 as a Cosmos chain."],
 [("Akash docs","https://akash.network/docs/")],"Akash Network")
coin("theta","theta-token","theta","Theta Network","THETA",["Media"],"#2AB8E6","#1B2B3C","Mar 2019","Mitch Liu and Jieyi Long","Multi BFT proof of stake",
 ["Theta Network is a blockchain for video streaming founded by Mitch Liu and Jieyi Long, building on their earlier streaming company. Viewers can share bandwidth and earn rewards. Its mainnet launched in March 2019, with THETA for staking and governance and TFUEL for fees."],
 [("Theta docs","https://docs.thetatoken.org/")],"Theta Network")
coin("axs","axie-infinity","axie-infinity","Axie Infinity","AXS",["Gaming"],"#0055D5","#00C2FF","2020","Trung Nguyen, Aleksander Larsen and others at Sky Mavis","Token on Ethereum and Ronin",
 ["Axie Infinity is a play to earn game from Vietnamese studio Sky Mavis, founded by Trung Nguyen and Aleksander Larsen. Players battle and breed NFT creatures called Axies. In 2021 it drew millions of players, especially in the Philippines.","In March 2022 attackers linked by the FBI to North Korea's Lazarus Group stole about 620 million dollars from the Ronin bridge."],
 [("FBI statement on the Ronin theft","https://www.fbi.gov/news/press-releases/fbi-statement-on-attribution-of-malicious-cyber-activity-posed-by-the-democratic-peoples-republic-of-korea")],"Axie Infinity",
 [E("2022-03-29","crash","Ronin bridge hack disclosed","About 620 million dollars is stolen from Axie's sidechain bridge.",["Sky Mavis disclosed on March 29, 2022 that the Ronin bridge had been drained on March 23 using stolen validator keys. The FBI later attributed the theft to North Korea's Lazarus Group."],[W("Axie Infinity"),("FBI statement on the Ronin theft","https://www.fbi.gov/news/press-releases/fbi-statement-on-attribution-of-malicious-cyber-activity-posed-by-the-democratic-peoples-republic-of-korea")])])
coin("mana","decentraland","decentraland","Decentraland","MANA",["Gaming","Metaverse"],"#FF2D55","#FFBC5B","Aug 2017","Ari Meilich and Esteban Ordano","Token on Ethereum",
 ["Decentraland is a virtual world on Ethereum where land parcels are NFTs bought with MANA. It was founded by Ari Meilich and Esteban Ordano, held its MANA token sale in August 2017 and opened to the public in February 2020.","Interest spiked in late 2021 when Facebook renamed itself Meta."],
 [("Decentraland docs","https://docs.decentraland.org/")],"Decentraland")
coin("sand","the-sandbox","the-sandbox","The Sandbox","SAND",["Gaming","Metaverse"],"#00ADEF","#0084FF","2020","Arthur Madrid and Sebastien Borget","Token on Ethereum and Polygon",
 ["The Sandbox is a voxel based virtual world and game builder, owned by Animoca Brands since 2018 and led by Arthur Madrid and Sebastien Borget. Players buy land and items as NFTs using SAND.","Like Decentraland, it surged in late 2021 during the metaverse hype after Facebook's rebrand to Meta."],
 [("The Sandbox docs","https://sandboxgame.gitbook.io/the-sandbox")],"The Sandbox (2012 video game)")
coin("zk","zksync","zksync","ZKsync","ZK",["Layer 2"],"#1E69FF","#8C8DFC","Jun 17, 2024","Alex Gluchowski and Alex Vlasov of Matter Labs","Validity rollup (ZK rollup) on Ethereum",
 ["ZKsync is an Ethereum layer 2 network built by Matter Labs, founded by Alex Gluchowski and Alex Vlasov. Its ZKsync Era network uses zero knowledge proofs to post batches of transactions to Ethereum.","The ZK token was airdropped on June 17, 2024."],
 [("ZKsync docs","https://docs.zksync.io/")],"ZKsync",
 [E("2024-06-17","launch","ZK airdrop","ZKsync launches the ZK token.",["The ZK token launched with an airdrop on June 17, 2024."],[("ZKsync docs","https://docs.zksync.io/")])])
coin("neo","neo","neo","Neo","NEO",["Layer 1"],"#00E599","#58BF00","2014 (as AntShares)","Da Hongfei and Erik Zhang","Delegated Byzantine fault tolerance (dBFT)",
 ["Neo was founded in China in 2014 as AntShares by Da Hongfei and Erik Zhang and renamed Neo in 2017. It was nicknamed the Chinese Ethereum. Neo uses two tokens: NEO for governance and GAS for fees. Neo N3, a major upgrade, launched in 2021."],
 [("Neo docs","https://docs.neo.org/")],"Neo (blockchain)")
coin("imx","immutable-x","immutable","Immutable","IMX",["Gaming","Layer 2"],"#17B5CB","#0D1B2A","2021","James Ferguson and Robbie Ferguson","Token for an Ethereum gaming layer 2",
 ["Immutable is an Australian company founded by brothers James and Robbie Ferguson that builds blockchain gaming infrastructure, including Immutable X and the zkEVM, and the game Gods Unchained. IMX launched in 2021."],
 [("Immutable docs","https://docs.immutable.com/")],"Immutable Pty Ltd")
coin("chz","chiliz","chiliz","Chiliz","CHZ",["Sports"],"#CD0124","#FF4D6D","2018","Alexandre Dreyfus","Proof of staked authority (Chiliz Chain)",
 ["Chiliz was founded in 2018 by French entrepreneur Alexandre Dreyfus and powers Socios, an app where sports clubs such as FC Barcelona sell fan tokens that give holders votes on minor club decisions. Chiliz later launched its own chain."],
 [("Chiliz docs","https://docs.chiliz.com/")],"Chiliz")
