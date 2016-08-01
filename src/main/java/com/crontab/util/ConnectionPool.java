package com.crontab.util;

import java.sql.Connection;
import java.sql.DriverManager;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class ConnectionPool {
	private static List<Connection> freeList = new ArrayList<Connection>();
	private static List<Connection> usedList = new ArrayList<Connection>();

	static {
		try {

			Class.forName("org.mariadb.jdbc.Driver");

			for (int i = 0; i < 5; i++) {
				freeList.add(DriverManager.getConnection("jdbc:mysql://14.32.66.116:10003/test_recode", "sl", "sl"));
			}

		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	public static Connection getConnection() throws Exception {
		if(freeList.isEmpty()){
			throw new Exception("대기중인 커넥션이 없습니다.");
		}
		// 대기 풀에서 꺼낸 다음 해당 객체를 삭제처리
		Connection con = freeList.remove(0);
		// 사용중인 풀로 이동
		usedList.add(con);
//		System.out.println("사용 중 개수 : " + usedList.size());
//		System.out.println("대기 중 남은 개수 : " + freeList.size());
		return con;
	}
	public static void release(Connection con) {
		// 사용중인 풀에서 제거하고 대기중인 풀로 이동
		usedList.remove(con);
		
		freeList.add(con);
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		try {
			
			for (int i = 1; i <= 6; i++) {
				System.out.print("프로그램 연결요청 들어옴");
				sc.nextLine();
				System.out.println(i + "번째 연결 요청");
				Connection con = ConnectionPool.getConnection();
				
				ConnectionPool.release(con);
			}
		} catch (Exception e){
			e.printStackTrace();
		}
	}
}
