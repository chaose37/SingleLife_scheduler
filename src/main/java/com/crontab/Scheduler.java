package com.crontab;

import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

import com.crontab.cvsInfo.ConnectionCVS;
import com.crontab.cvsInfo.ConnectionPlay;
import com.crontab.cvsInfo.ConnectionProductInfo;
import com.crontab.cvsInfo.ConnectionResturant;
import com.crontab.cvsInfo.ConnectionRecipe;

@Component
public class Scheduler {
	/**
	 * 편의점 매달 1일 오전 07:00:00에 호출이 되는 스케쥴러
	 */
	@Scheduled(cron = "0 00 07 1 * *")
	public void CVSInfo() {
		System.out.println("CVSInfo Start");
		try {
			System.out.println("CVS Info Delete");
			ConnectionCVS.deleteCVS();
			
			System.out.println("GS Info Insert");
			ConnectionCVS.insertGS();
			System.out.println("End");
			
			System.out.println("CU Info Insert");
			ConnectionCVS.cuInfo();
			System.out.println("End");
			
			System.out.println("7eleven Info Insert");
			ConnectionCVS.sevenInfo();
			System.out.println("End");
			
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	/**
	 * 웹툰 매일 오전 00:00:00에 호출이 되는 스케쥴러
	 */
	@Scheduled(cron = "0 00 00 * * *")
	public void webtoon() {
		System.out.println("Start");
		
		try {
			System.out.println("Webtoon Delete");
			ConnectionPlay.deleteWebtoon();
			
			System.out.println("Naver Webtoon Insert");
			ConnectionPlay.insertNaver();
			System.out.println("End");
			
			System.out.println("Daum WebToon Insert");
			ConnectionPlay.insertDaum();
			System.out.println("End");
			
		} catch(Exception e) {
			e.printStackTrace();
		}
	}

	/**
	 * Youtube 매일 오전 00:00:00에 호출이 되는 스케쥴러
	 */
	@Scheduled(cron = "0 00 00 * * *")
	public void youtube() {
		System.out.println("Start");
		
		try {
			System.out.println("Youtube Delete");
			ConnectionPlay.deleteYouTube();
			
			System.out.println("Youtube Insert");
			ConnectionPlay.insertYouTube();
			System.out.println("End");
			
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	/**
	 * Game 매달 1일 오전 00:00:00에 호출이 되는 스케쥴러
	 */
	@Scheduled(cron = "0 00 00 1 * *")
	public void game() {
		System.out.println("Start");
		
		try {
			System.out.println("Game Delete");
			ConnectionPlay.deleteGame();
			
			System.out.println("Game Insert");
			ConnectionPlay.insertGame();
			System.out.println("End");
			
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	/**
	 * 여행 매달 1일 오전 00:00:00에 호출이 되는 스케쥴러
	 */
	@Scheduled(cron = "0 00 00 1 * *")
	public void travel() {
		System.out.println("Start");
		
		try {
			System.out.println("Webtoon Delete");
			ConnectionPlay.deleteWebtoon();
			
			System.out.println("Naver Webtoon Insert");
			ConnectionPlay.insertNaver();
			System.out.println("End");
			
			System.out.println("Daum Webtoon Insert");
			ConnectionPlay.insertDaum();
			System.out.println("End");
			
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	/**
	 * 맛집 매달 1일 오전 00:00:00에 호출이 되는 스케쥴러
	 */
	@Scheduled(cron = "0 00 00 1 * *")
	public void resturant() {
		System.out.println("Start");
		
		try {
			System.out.println("Returant Delete");
			ConnectionResturant.deleteResturant();
			
			System.out.println("Naver Resturant Insert");
			ConnectionResturant.insertNaverResturant();
			System.out.println("End");
			
			System.out.println("Daum Resturant Insert");
			ConnectionResturant.insertDaumResturant();
			System.out.println("End");
			
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	/**
	 * 1인용 상품 매일 오전 00:00:00에 호출이 되는 스케쥴러
	 */
	@Scheduled(cron = "0 00 00 * * *")
	public void productInfo() {
		System.out.println("Start");
		
		try {
			System.out.println("Product Delete");
			ConnectionProductInfo.deleteProduct();
			
			System.out.println("Auction Insert");
			ConnectionProductInfo.insertAuction();
			System.out.println("End");
			
			System.out.println("Coupang Insert");
			ConnectionProductInfo.insertCoupang();
			System.out.println("End");
			
			System.out.println("TicketMonster Insert");
			ConnectionProductInfo.insertTicketMonster();
			System.out.println("End");
			
			System.out.println("WemakePrice Insert");
			ConnectionProductInfo.insertWemakePrice();
			System.out.println("End");
			
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	/**
	 * 1인분 레시피 매달 오전 00:00:00에 호출이 되는 스케쥴러
	 */
	@Scheduled(cron = "0 00 00 1 * *")
	public void recipeInfo() {
		System.out.println("Start");
		
		try {
			System.out.println("Recipe Delete");
			ConnectionRecipe.deleteSingleFood();
			
			System.out.println("NaverRecipe Insert");
			ConnectionRecipe.insertNaverFood();
			System.out.println("End");
			
			System.out.println("DaumRecipe Insert");
			ConnectionRecipe.insertDaumFood();
			System.out.println("End");
			
		} catch(Exception e) {
			e.printStackTrace();
		}
	}

}