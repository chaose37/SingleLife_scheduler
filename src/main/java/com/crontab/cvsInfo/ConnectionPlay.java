package com.crontab.cvsInfo;

import java.sql.Connection;
import java.sql.PreparedStatement;

import com.crontab.util.ConnectionPool;

public class ConnectionPlay {
	public static void deleteWebtoon() throws Exception {
		Connection con = null;
		PreparedStatement pstmt = null;
		
		try {
			con = ConnectionPool.getConnection();

			String sql = "delete from sl_play where category='Webtoon'";
			
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

	public static void deleteYouTube() throws Exception {
		Connection con = null;
		PreparedStatement pstmt = null;
		
		try {
			con = ConnectionPool.getConnection();
			
			String sql = "delete from sl_play where category='Youtube'";
			
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
	
	public static void deleteGame() throws Exception {
		Connection con = null;
		PreparedStatement pstmt = null;
		
		try {
			con = ConnectionPool.getConnection();
			
			String sql = "delete from sl_play where category='Game'";
			
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
	
	public static void insertYouTube() {
		String directory = "python C://Users//Hong//PycharmProjects//untitled//youtube-mv.py";
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
	
	public static void insertNaver() {
		String directory = "python C://Users//Hong//PycharmProjects//untitled//naverWebtoon.py";
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
	
	public static void insertDaum() {
		String directory = "python C://Users//Hong//PycharmProjects//untitled//daumWebToon.py";
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
	
	public static void insertGame() {
		String directory = "python C://Users//Hong//PycharmProjects//untitled//iogames.py";
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
