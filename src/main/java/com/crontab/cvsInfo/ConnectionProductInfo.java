package com.crontab.cvsInfo;

import java.sql.Connection;
import java.sql.PreparedStatement;

import com.crontab.util.ConnectionPool;

public class ConnectionProductInfo {
	public static void deleteProduct() throws Exception {
		Connection con = null;
		PreparedStatement pstmt = null;
		
		try {
			con = ConnectionPool.getConnection();

			String sql = "delete from sl_prodInfo";
			
			pstmt = con.prepareStatement(sql);
			pstmt.executeUpdate();
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			if(pstmt != null) {
				pstmt.close();
			}
			if (con != null) {
				con.close();
			}
		}
	}
	
	public static void insertAuction() {
		String directory = "python C://Users//Hong//PycharmProjects//untitled//auctionProd.py";
		Runtime rt = Runtime.getRuntime();
		
		Process p;
		try {
			p = rt.exec(directory);
			p.getErrorStream().close();
			p.getInputStream().close();
			p.getOutputStream().close();
			p.waitFor();
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public static void insertCoupang() {
		String directory = "python C://Users//Hong//PycharmProjects//untitled//coupang.py";
		Runtime rt = Runtime.getRuntime();
		
		Process p;
		try {
			p = rt.exec(directory);
			p.getErrorStream().close();
			p.getInputStream().close();
			p.getOutputStream().close();
			p.waitFor();
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public static void insertTicketMonster() {
		String directory = "python C://Users//Hong//PycharmProjects//untitled//tmon.py";
		Runtime rt = Runtime.getRuntime();
		
		Process p;
		try {
			p = rt.exec(directory);
			p.getErrorStream().close();
			p.getInputStream().close();
			p.getOutputStream().close();
			p.waitFor();
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public static void insertWemakePrice() {
		String directory = "python C://Users//Hong//PycharmProjects//untitled//wmpProd.py";
		Runtime rt = Runtime.getRuntime();
		
		Process p;
		try {
			p = rt.exec(directory);
			p.getErrorStream().close();
			p.getInputStream().close();
			p.getOutputStream().close();
			p.waitFor();
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
}
